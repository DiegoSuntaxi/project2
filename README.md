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
<h5>Scraping Tarea 1 </h5>
<h5>Interfaz web para búsqueda de establecimientos mediante API
</h5>
<ul>
<li>La imagen muestra una interfaz web interactiva que permite buscar establecimientos como hospitales, farmacias o restaurantes a partir de una ubicación geográfica (latitud, longitud y radio). La aplicación consume un endpoint GET de la API desarrollada, ejecutada en entorno local, y devuelve los resultados de forma dinámica según los parámetros seleccionados por el usuario.</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_11.jpeg" width="500">
  
</p>
<h5>Consumo del API para búsqueda de establecimientos por ubicación</h5>
<ul>
<li>El código muestra el uso de las librerías requests y pandas para consumir un endpoint GET del API local, enviando parámetros de ubicación (latitud, longitud y radio) y realizando consultas por distintos tipos de establecimientos como restaurantes, hospitales y farmacias, con el fin de procesar posteriormente los datos obtenidos.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_12.jpeg" width="500">
</p>
<h5>Consulta iterativa al API y consolidación de resultados</h5>
<ul>
<li>El código realiza múltiples peticiones GET al API local para distintos tipos de establecimientos, combina los resultados en una sola estructura de datos y los organiza en un DataFrame de pandas, añadiendo además enlaces directos a Google Maps a partir de la ubicación geográfica obtenida.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_13.jpeg" width="500">
</p>
<h5>Visualización final de datos enriquecidos</h5>
<ul>
<li>La imagen muestra el DataFrame final en pandas con los establecimientos obtenidos desde el API, incluyendo campos como nombre, dirección, calificación, ubicación y un enlace directo a Google Maps, lo que facilita la visualización y consulta geográfica de los resultados.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_14.jpeg" width="500">
</p>
<h5>Exportación final de datos procesados</h5>
<ul>
<li>La imagen muestra el DataFrame final con información enriquecida (enlaces, horarios y ubicación) y el proceso de exportación de los datos a formatos CSV y Excel, completando el flujo de extracción, procesamiento y almacenamiento de la información.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_15.jpeg" width="500">
</p>
<h5>Datos finales consolidados en formato Excel</h5>
<ul>
<li>La imagen muestra el archivo Excel final que contiene los datos extraídos y procesados, organizados en columnas como nombre del establecimiento, dirección, calificación, número de usuarios, ubicación geográfica, horarios y enlaces a Google Maps, facilitando su revisión y análisis de forma tabular.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_16.jpeg" width="500">
</p>
<h5>Archivo CSV con datos procesados en formato crudo</h5>
<ul>
<li>La imagen muestra el contenido del archivo CSV final, donde los datos de establecimientos (nombre, dirección, calificación, ubicación, horario, tipo y enlaces) aparecen consolidados en una sola fila por registro, reflejando el resultado directo de la exportación del procesamiento realizado en el proyecto.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_17.jpeg" width="500">
</p>

<h5>Scraping Tarea 2 - Ejemplo 2</h5>
<h5>Codigo API</h5>
<ul>
<li>El código muestra la configuración de un entorno de web scraping con Selenium, donde se utiliza un navegador automatizado para acceder a una API (http://localhost:8000). Esta integración permite consumir datos del servicio, procesarlos posteriormente y almacenarlos de forma estructurada dentro del proyecto.</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_1.jpeg" width="500">
  
</p>
<h5>Extracción y estructuración de datos HTML con BeautifulSoup</h5>
<ul>
<li>El código procesa el contenido HTML obtenido mediante Selenium utilizando BeautifulSoup, extrae datos estructurados de cada tarjeta (nombre, horario, dirección, calificación y usuarios) y los almacena en una lista de diccionarios, que luego se imprime y sirve como base para su posterior guardado en CSV.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_2.jpeg" width="500">
</p>
<h5>Resultados de los datos extraídos</h5>
<ul>
<li>La imagen muestra la salida de datos estructurados obtenidos mediante web scraping, donde se listan varios establecimientos con información como nombre, horario, dirección, calificación y número de usuarios, almacenados en una estructura tipo diccionario.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_3.jpeg" width="500">
</p>
<h5>Tabla de datos procesados</h5>
<ul>
<li>La imagen muestra los datos extraídos y procesados convertidos en un DataFrame de pandas, donde se organizan campos como nombre, horario, dirección, calificación y número de usuarios, facilitando su visualización y posterior exportación a formatos como CSV o Excel.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_4.jpeg" width="500">
</p>
<h5>Generación y vista previa del archivo CSV</h5>
<ul>
<li>La imagen muestra la exportación de los datos procesados a un archivo CSV, junto con una vista previa del contenido generado, confirmando que la información extraída fue correctamente estructurada y guardada para su uso final.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_5.jpeg" width="500">
</p>
<h5>Guardado final de datos en CSV</h5>
<ul>
<li>La imagen muestra la exportación final de los datos extraídos a un archivo CSV (lugares_scrapeados.csv), utilizando pandas, y el cierre correcto del navegador automatizado, dando por finalizado el proceso de web scraping.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_6.jpeg" width="500">
</p>
<h5>Contenido del archivo CSV generado</h5>
<ul>
<li>La La imagen muestra el contenido del archivo CSV generado, donde se almacenan los datos finales obtenidos del scraping, organizados por columnas como nombre, horario, dirección, calificación y número de usuarios, listos para su uso y análisis.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte2_7.jpeg" width="500">
</p>
<h5>historial de commits del repositorio en GitHub</h5>

<p align="center">
  <img src="Evidencias/Parte2_8.png" width="500">
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

