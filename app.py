from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import time
import googlemaps
import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

API_KEY = os.getenv("GOOGLE_API_KEY_2")

if not API_KEY:
    raise ValueError("No se encontró la variable de entorno GOOGLE_API_KEY_2")

gmaps = googlemaps.Client(key=API_KEY)


def get_places(lat: float, lng: float, radius: int = 1000, place_type: str = "restaurant"):
    location = (lat, lng)

    results_list = []
    max_requests = 3
    request_count = 0

    response = gmaps.places_nearby(
        location=location,
        radius=radius,
        type=place_type
    )

    while response:
        for place in response.get("results", []):
            geometry = place.get("geometry", {}).get("location", {})
            place_id = place.get("place_id")
            photos = place.get("photos", [])
            photo_url = "/static/imagen.jpg" 
            if photos:
                photo_ref = photos[0].get("photo_reference")
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={API_KEY}"
            horario_hoy = "Horario no disponible"
            try:
                details = gmaps.place(place_id=place_id, fields=["opening_hours"], language="es")
                opening_hours = details.get("result", {}).get("opening_hours")
                if opening_hours and "weekday_text" in opening_hours:
                    weekday_text = opening_hours.get("weekday_text", [])
                    dia_actual = datetime.datetime.today().weekday()
                    horario_crudo = weekday_text[dia_actual]
                    if ":" in horario_crudo:
                        horario_hoy = horario_crudo.split(":", 1)[1].strip()
                    else:
                        horario_hoy = horario_crudo
            except Exception as e:
                print(f"Error con el horario de {place.get('name')}: {type(e).__name__} - {e}")
            results_list.append({
                "name": place.get("name"),
                "address": place.get("vicinity"),
                "rating": place.get("rating"),
                "users": place.get("user_ratings_total"),
                "price_level": place.get("price_level"),
                "lat": geometry.get("lat"),
                "lng": geometry.get("lng"),
                "photo_url": photo_url,
                "today_hours": horario_hoy
            })

        request_count += 1
        if request_count >= max_requests:
            break

        next_page_token = response.get("next_page_token")
        if next_page_token:
            time.sleep(2)
            response = gmaps.places_nearby(page_token=next_page_token)
        else:
            break

    return results_list


@app.get("/api/restaurants")
def restaurants_api(
    lat: float = Query(...),
    lng: float = Query(...),
    radius: int = Query(1000, ge=1, le=50000),
    type: str = Query("restaurant")
):
    try:
        return get_places(lat=lat, lng=lng, radius=radius, place_type=type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo lugares: {str(e)}")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "maps_api_key": API_KEY}
    )