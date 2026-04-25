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
  <li>FastAPI</li>
  <li>Uvicornli>
  <li>Pydantic</li>
  <li>Requests</li>
  <li>Google Maps / Google Places API</li>
  <li>Jinja2</li>
  <li>Python</li>
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
  <img src="Evidencias/Parte1_10.PNG" width="500">
  <img src="Evidencias/Parte1_11.PNG" width="500">
  <img src="Evidencias/Parte1_12.PNG" width="500">
  
</p>
<h5>Codificación de la interfaz web para consulta de establecimientos desde el mapa</h5>
<ul>
<li>El código implementa una interfaz web interactiva que utiliza Google Maps para seleccionar una ubicación mediante clic y consultar establecimientos cercanos a través de un endpoint del API. Los resultados se obtienen usando fetch, se procesan dinámicamente y se muestran en tarjetas con información relevante y enlaces directos a Google Maps.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_13.PNG" width="500">
  <img src="Evidencias/Parte1_14.PNG" width="500">
  <img src="Evidencias/Parte1_15.PNG" width="500">
  <img src="Evidencias/Parte1_16.PNG" width="500">
  
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
<h5>Web scraping y exportación de datos
</h5>
<ul>
<li>El código implementa un proceso de web scraping con Selenium y BeautifulSoup para extraer información de establecimientos desde una interfaz web dinámica. Los datos obtenidos se procesan y estructuran con pandas en un DataFrame y finalmente se exportan a formatos CSV y Excel, permitiendo su almacenamiento y análisis posterior.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Parte1_17.PNG" width="500">
  <img src="Evidencias/Parte1_18.PNG" width="500">
  <img src="Evidencias/Parte1_19.PNG" width="500">
</p>


<h5>Historial de commits y control de versiones del proyecto
</h5>
<ul>
<li>La imagen muestra la ejecución de una consulta desde la interfaz web hacia el API local, visualizada mediante las herramientas de desarrollador del navegador. Se evidencia una petición GET exitosa (HTTP 200) al endpoint del API con parámetros de latitud, longitud, radio y tipo de lugar, confirmando la correcta comunicación entre el frontend y el backend del proyecto.
</li>
</ul>
<p align="center">
  <img src="Evidencias/Branch.PNG" width="500">
</p>

<hr>
<h3>Preguntas trabajo final</h3>

<p>
  <strong>1. ¿Cómo podría un atacante manipular estos parámetros para forzar consultas excesivas o anómalas a la API externa, y qué impacto tendría esto en términos de costo, disponibilidad y posible bloqueo del servicio?</strong>
</p>

<p>
Un atacante podría manipular parámetros enviados a la API, como búsquedas, coordenadas, filtros, radios de búsqueda, páginas, límites de resultados o tipos de consulta, con el objetivo de generar una gran cantidad de solicitudes hacia una API externa. Por ejemplo, podría enviar valores muy amplios, repetir peticiones automáticamente o modificar parámetros para consultar zonas muy grandes o con demasiados resultados.
</p>

<p>
Esto podría provocar un consumo excesivo de recursos y generar varios impactos negativos:
</p>

<ul>
  <li><b>Costo:</b> si la API externa cobra por número de consultas, el uso abusivo puede generar cargos elevados.</li>
  <li><b>Disponibilidad:</b> el servidor puede saturarse por exceso de solicitudes, afectando a los usuarios legítimos.</li>
  <li><b>Bloqueo del servicio:</b> la API externa puede detectar comportamiento anómalo y bloquear la clave API o la IP del servidor.</li>
  <li><b>Rendimiento:</b> las respuestas pueden volverse lentas o fallar por sobrecarga.</li>
</ul>

<p>
Para mitigar este riesgo, se deben validar estrictamente los parámetros recibidos, limitar rangos permitidos, implementar autenticación, aplicar rate limiting, controlar el número máximo de resultados, usar caché para consultas repetidas y registrar actividad sospechosa.
</p>


<p>
  <strong>2. ¿Cómo podría un atacante insertar contenido malicioso en la página origen para que, tras el scraping y almacenamiento en CSV, ese contenido termine ejecutándose en el navegador de los usuarios al visualizar los resultados en la interfaz web?</strong>
</p>

<p>
Un atacante podría insertar contenido malicioso en la página origen que posteriormente será extraída mediante web scraping. Por ejemplo, podría incluir código HTML o JavaScript dentro de campos como títulos, descripciones o comentarios.
</p>

<p>
Si el scraper obtiene ese contenido y lo guarda directamente en un archivo CSV sin ningún tipo de validación o limpieza, y luego la aplicación web muestra esos datos tal como fueron obtenidos, el navegador podría interpretar ese contenido como código ejecutable en lugar de texto. Este tipo de ataque se conoce como <b>Cross-Site Scripting almacenado</b> (Stored XSS).
</p>

<p>
Ejemplo de contenido malicioso:
</p>

<pre><code class="language-html">
&lt;script&gt;alert("Ataque XSS")&lt;/script&gt;
</code></pre>

<p>
El problema ocurre cuando la aplicación web presenta esta información utilizando métodos inseguros (por ejemplo, insertando directamente el contenido en el HTML), lo que permite que el navegador ejecute el script.
</p>

<p>
Las consecuencias pueden incluir robo de información, secuestro de sesiones, redirecciones a sitios maliciosos o ejecución de acciones no autorizadas en nombre del usuario.
</p>

<p>
Para prevenir este problema, se deben aplicar medidas como:
</p>

<ul>
  <li>Validar y limpiar los datos obtenidos durante el scraping.</li>
  <li>Tratar siempre los datos externos como no confiables.</li>
  <li>Mostrar la información como texto y no como código ejecutable.</li>
  <li>Evitar insertar directamente contenido dinámico en el HTML sin control.</li>
  <li>Implementar políticas de seguridad en la aplicación web.</li>
</ul>

<p>
De esta manera, aunque la página origen contenga contenido malicioso, este será tratado únicamente como texto y no se ejecutará en el navegador de los usuarios.
</p>


<hr>
<h3>Comentario</h3>
<p>
Las imágenes incluidas documentan visualmente todo el desarrollo del proyecto, desde la configuración de las APIs de Google Maps y Google Places en Google Cloud, la creación y gestión de credenciales, hasta el funcionamiento de la interfaz web y el consumo del API local. Asimismo, se evidencian los resultados obtenidos al realizar búsquedas geolocalizadas de distintos tipos de establecimientos y el historial de commits en GitHub, lo que demuestra la correcta implementación del sistema, el uso de buenas prácticas de desarrollo y el trabajo colaborativo realizado durante el proyecto.
</p>

<h2>Conclusiones</h2>
<ul>
  <li>El proyecto permitió desarrollar una solución completa basada en una API funcional, integrando tecnologías como FastAPI, Google Maps API y Google Places API, logrando una búsqueda geolocalizada de establecimientos de manera eficiente y estructurada.</li>
  <li>A través del uso de web scraping y procesamiento de datos, se obtuvo información relevante que fue limpiada, estructurada y almacenada en formatos estándar como CSV y Excel, facilitando su reutilización y análisis.</li>
  <li>La implementación de una interfaz web interactiva mejoró la usabilidad del sistema, permitiendo al usuario seleccionar ubicaciones directamente desde un mapa y visualizar los resultados de forma clara mediante tarjetas informativas.</li>
  <li>La correcta configuración de credenciales y habilitación de APIs en Google Cloud fue un aspecto clave para garantizar el funcionamiento seguro y estable de los servicios utilizados en el proyecto.</li>
  <li>El uso de GitHub como sistema de control de versiones permitió evidenciar un trabajo colaborativo organizado, con historial de commits, manejo de ramas y resolución de conflictos, reflejando buenas prácticas de desarrollo de software.
</li>
</ul>
<hr>

