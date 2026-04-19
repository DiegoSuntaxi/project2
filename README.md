<p align="center">
  <img src="Evidencias/logo-uide.webp" width="220" alt="Logo UIDE">
</p>

<h1 align="center">Laboratorio 2 - Grupo 6</h1>

<p align="center">
  <b>MCIB-B</b><br>
  Trabajo grupal enfocado en el proceso de web scraping en entorno local
</p>
<h2>Integrantes</h2>

<ul>
  <li>AMAGUA OSCAR</li>
  <li>OJEDA ALAN</li>
  <li>SUNTAXI DIEGO</li>
</ul>
<hr>

<h2>Introducción</h2>
<p>
En el presente proyecto se desarrolló una API funcional utilizando FastAPI, orientada a la consulta de establecimientos cercanos como bancos, farmacias, restaurantes y hospitales a partir de una ubicación geográfica seleccionada por el usuario. La solución combina el consumo de datos externos, el procesamiento de información y su exposición mediante servicios web, aplicando buenas prácticas de desarrollo, versionamiento y despliegue en entorno local.
  
La API se complementa con una interfaz web interactiva, accesible desde localhost, que integra un mapa dinámico donde el usuario puede seleccionar una ubicación específica y definir parámetros de búsqueda como el radio y el tipo de establecimiento. A partir de estos parámetros, la aplicación consume los endpoints del API y devuelve los resultados de forma estructurada y visual.

Como parte del flujo de trabajo, se realizó un proceso previo de recolección y tratamiento de datos mediante web scraping, cuyos resultados se almacenan en formatos estándar como CSV y Excel, permitiendo su reutilización y análisis. El proyecto se encuentra organizado en un repositorio que incluye el código fuente del API, la interfaz web, los notebooks de pruebas, los archivos de datos procesados y la documentación correspondiente.

Finalmente, se utilizó GitHub como sistema de control de versiones y colaboración, registrando los cambios realizados durante el desarrollo y asegurando la trazabilidad del proyecto. Esta implementación demuestra un flujo completo que abarca desde la obtención de datos hasta su exposición mediante una API y su consumo a través de una aplicación web funcional.
</p>

<hr>

<h2>Objetivo</h2>
<p>
Diseñar, construir y desplegar un API funcional, aplicando buenas prácticas de desarrollo, versionamiento, pruebas y despliegue local usando FastAPI.
</p>

<hr>

<h2>Parte 1 – Construcción del API</h2>

<h3>Repositorio del proyecto</h3>
<ul>
  
  <li>Código fuente del API desarrollado con FastAPI</li>
  <li>Interfaz web basada en HTML que consume el API y permite la búsqueda de establecimientos desde un mapa interactivo</li>
  <li>Archivos estáticos y plantillas (static/, templates/)</li>
  <li>Archivo app.py con la lógica principal del servicio</li>
  <li>Archivo README.md con la documentación del proyecto</li>
  <li>Carpeta Evidencias/ con capturas o pruebas del funcionamiento</li>
  <li>Versión en formato Excel de los datos finales.</li>
  
</ul>

<h3>API funcional</h3>
<ul>
  <li>jupyter</li>
  <li>selenium</li>
  <li>pandas</li>
  <li>time</li>
</ul>

<h3>Creatividad/Dificultad</h3>
<ul>
  
<li>Integración con APIs externas</li>
<li>Procesamiento de datos</li>
<li>Demos de Soluciones tecnologicas</li>
</ul>

<h3>Evidencia</h3>
<h5>Construcción del API </h5>
<h5>API de búsqueda geolocalizada</h5>
<ul>
<li>El código implementa una API con FastAPI que consume la API de Google Places para buscar establecimientos cercanos según ubicación, radio y tipo de lugar. Procesa los resultados para extraer información relevante como nombre, dirección, calificación, horario actual y una imagen representativa, y expone estos datos mediante un endpoint GET y una interfaz web basada en plantillas HTML.</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_10.jpeg" width="500">
  <img src="Evidencias/Parte1_11.jpeg" width="500">
  <img src="Evidencias/Parte1_12.jpeg" width="500">
  
</p>
<h5>Codificación de la interfaz web para consulta de establecimientos desde el mapa</h5>
<ul>
<li>El código implementa una interfaz web interactiva que utiliza Google Maps para seleccionar una ubicación mediante clic y consultar establecimientos cercanos a través de un endpoint del API. Los resultados se obtienen usando fetch, se procesan dinámicamente y se muestran en tarjetas con información relevante y enlaces directos a Google Maps.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_13.jpeg" width="500">
  <img src="Evidencias/Parte1_14.jpeg" width="500">
  <img src="Evidencias/Parte1_15.jpeg" width="500">
  <img src="Evidencias/Parte1_16.jpeg" width="500">
  
</p>
<h5>Resultados visuales de búsqueda geolocalizada de establecimientos
</h5>
<ul>
<li>La interfaz web permite seleccionar una ubicación directamente en el mapa, definir un radio de búsqueda y elegir el tipo de establecimiento. A partir de estos parámetros, la aplicación consulta el API local y muestra los resultados de forma dinámica, facilitando la exploración de lugares cercanos como bancos, farmacias o restaurantes.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_1.jpeg" width="500">
  <img src="Evidencias/Parte1_2.jpeg" width="500">
  <img src="Evidencias/Parte1_3.jpeg" width="500">
  <img src="Evidencias/Parte1_4.jpeg" width="500">
  <img src="Evidencias/Parte1_5.jpeg" width="500">
</p>
<h5>Habilitación de Google Maps JavaScript API</h5>
<ul>
<li>La imagen muestra la activación de la API de Google Maps JavaScript en la consola de Google Cloud, la cual permite integrar mapas interactivos en la aplicación web. Esta configuración es fundamental para visualizar el mapa, capturar la ubicación seleccionada por el usuario y habilitar la interacción geográfica utilizada por el API del proyecto.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_6.jpeg" width="500">
</p>
<h5>Habilitación de Google Places API
</h5>
<ul>
<li>La imagen muestra la activación de la API de Google Places en la consola de Google Cloud, necesaria para obtener información detallada de establecimientos como nombre, dirección, calificación y horarios. Esta API es utilizada por el backend del proyecto para realizar búsquedas geolocalizadas y alimentar los resultados consultados desde el API y la interfaz web.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_7.jpeg" width="500">
</p>
<h5>Creación y gestión de la clave de API de Google Maps Platform
</h5>
<ul>
<li>La imagen muestra la creación y administración de una clave de API en Google Cloud, utilizada para autenticar el acceso a los servicios de Google Maps y Google Places. Esta clave es esencial para que la aplicación pueda consumir las APIs habilitadas de forma segura y controlar su uso mediante restricciones configuradas.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_8.jpeg" width="500">
</p>
<h5>Consumo del API local desde la interfaz web
</h5>
<ul>
<li>La imagen muestra la ejecución de una consulta desde la interfaz web hacia el API local, visualizada mediante las herramientas de desarrollador del navegador. Se evidencia una petición GET exitosa (HTTP 200) al endpoint del API con parámetros de latitud, longitud, radio y tipo de lugar, confirmando la correcta comunicación entre el frontend y el backend del proyecto.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_9.jpeg" width="500">
</p>


<h3>Comentario</h3>
<p>
El proyecto abarcó la extracción, limpieza y almacenamiento de datos mediante web scraping, integrando una API local y utilizando GitHub para el control de versiones y el trabajo colaborativo, siguiendo un flujo de desarrollo ordenado y reproducible.
</p>

<h2>Conclusiones</h2>
<ul>
  <li>El proyecto permitió aplicar de manera práctica un flujo completo de tratamiento de datos, desde la extracción mediante web scraping hasta el almacenamiento final en formatos estructurados como CSV y Excel.</li>
  <li>El uso de herramientas como Selenium, BeautifulSoup y pandas facilitó la automatización, limpieza y organización de los datos, mejorando su calidad y utilidad para futuros análisis.</li>
  <li>La integración de una API funcional en entorno local demostró cómo los datos procesados pueden ser expuestos y consumidos por otros sistemas, fortaleciendo la arquitectura del proyecto.</li>
  <li>La utilización de GitHub como sistema de control de versiones permitió un trabajo ordenado y colaborativo, evidenciando la importancia de los commits y la documentación en proyectos de desarrollo.</li>
  <li>En conjunto, el proceso seguido refleja buenas prácticas en la gestión de datos y desarrollo de software, asegurando un trabajo reproducible, organizado y alineado con entornos reales.
</li>
</ul>
<hr>

