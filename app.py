from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import time
import googlemaps

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

            results_list.append({
                "name": place.get("name"),
                "address": place.get("vicinity"),
                "rating": place.get("rating"),
                "users": place.get("user_ratings_total"),
                "price_level": place.get("price_level"),
                "lat": geometry.get("lat"),
                "lng": geometry.get("lng")
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