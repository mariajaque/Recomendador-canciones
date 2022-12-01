# Recomendador-canciones
En este repositorio se encuentra un recomendador de canciones en función de diversas categorías como el artista, el género, la popularidad y el año de lanzamiento.

Para ello, el repositorio cuenta con los siguientes archivos necesarios para la ejecución:
- **"requirements.txt"**: contiene un listado de todas las librerías necesarias para la correcta ejecución del código.
- **"songs_normalize.csv"**: contiene información relativa a numerosos títulos de canciones como por ejemplo su autor o su popularidad.
- **"recomendador.py"**: contiene el código necesario para poder recomendar. Emplea una estructura de ETL en la cuál primero extrae todos los valores del fichero ".csv", posteriormente los transforma hasta quedarse únicamente con aquellos que satisfacen los criterios de búsqueda y filtrado de canciones del usuario y finalmente los devuelve por pantalla.


### Ejecución del Código:

Primero debe hacerse un pip install - r requirements.txt para que se instalen en el dispositivo las librerías necesarías para la ejecución del código. Posteriormente ya podrá ejecutarse el fichero "recomendador.py". Al ejecutar el ".py" se solicita al usuario que introduzca el nombre de la categoría por la que desea realizar la recomendación. Una vez seleccionada una categoría válida se muestran los filtros posibles dentro de la misma (por ejemplo si se introduce la categoría "artist" se mostrarán todos los artistas que tienen canciones en el fichero ".csv"). Finalmente debe de introducirse el nombre de alguno de los filtros (por ejemplo el nombre de un autor) y el programa mostrará por pantalla todas las canciones que cumplan esos criterios de búsqueda.
