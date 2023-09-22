# Proyecto de Análisis de Datos y Sistema de Recomendación




Este proyecto tiene como objetivo principal realizar un análisis de datos en un conjunto de datos relacionado con reseñas de juegos y desarrollar un sistema de recomendación basado en este análisis, construir un API y un Modelo Machine Learning. 

A continuación, se detallan los pasos y requerimientos para llevar a cabo este proyecto.

## Transformaciones de Datos y Análisis Exploratorio de los Datos (EDA)


En esta fase inicial del proyecto, se debe realizar un análisis exploratorio de los datos para investigar las relaciones entre las variables del conjunto de datos y si se requiere realizar transformaciones de datos. Sin embargo, se debe garantizar que el conjunto de datos se lea con el formato correcto y se pueden eliminar columnas innecesarias o solo trabajar con aquellas columnas que nos permitan optimizar el rendimiento de la API y el entrenamiento del modelo. **Esto ultimo fue lo que se decidio realizar**.

Luego de visualizar los datos en los 3 archivos dados (cabe resaltar que fueron de tipo **JSON** y pueden ser encontrados en el siguiente enlace https://drive.google.com/drive/folders/11-QXtPVj0q3Uds45IOByNn7jreSHuBtg?usp=drive_link ), se procedio a crear DF independiente a partir de las columnas que nos interesaban en cada uno de ellos para realizar las funciones solicitadas y guarados commo archivos **CSV** que hacen mas facil su manipulacion y de menos espacio en memeoria.

Todo esto se realizo con Python y mayormente con la libreria Pandas.


### A continuacion detallo cada funcion y la estructura de datos que se usaron para su armado.


- userdata(User_id: str): Devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a las reseñas y la cantidad de items.

Para esta funcion utilizamos el archivo de items ali extrajimos datos de columnas anidadas las cuales desanidamos y le dimos el formato necesario hazta crear un DF limpio de este. Tambien usamos parte del archivo games, de la columna reviews que se encontraba anidada y luego de desanidar se procedio a  transformar esos datos en columnas separadas, utilizamos una de esas columnas independiente llamada price para obtener el costo de los gastos la cual concatenemos al DF de items limpio previamente obtenido.

- countreviews(YYYY-MM-DD y YYYY-MM-DD: str): Devuelve la cantidad de usuarios que realizaron reseñas entre las fechas proporcionadas y el porcentaje de recomendación basado en las reseñas.

Para esta funcion utilizamos el archivo de items de la columa de su mismo nombre que previamente desanidamos y que obtenimos columnas independientes alli encontramos una columna llan¡mada posted. En dicha columna se encontraban los datos con las fechas que debiamos utilizar para esta funcion la cual debios dar formato solicitado. para ello eliminamos parte del valor inicial del dato como era la palabra *posted*, luego separamos cada parte de la fecha en columnas diferentes para poder aplicar algunas mejoras como llevar el valor de los meses de letras a numeros, los dias en formato de dos numeros y alli nos percatamos que le año tenia valores faltantes que procedimos a rellenar con la moda obrtenida del conjunto de datos existentes para el año. Tambien de las columnas independientes utilizamos la columna recommend la cual llevamos de valores booleanos a numericos donde True es 1 y False es 0.


- genre(género: str): Devuelve la posición en la que se encuentra un género en el ranking de géneros, analizado bajo la columna 'PlayTimeForever'.

Aca utilizamos Df del archivos items y Df del archivos games, que luefo fueron unidos con un *inner join* por la columna user_id que ambos compartian  para obtener los datos de genero de juego.

El DF que se construyo del archivo items fue obtenido del DF desanidado previamente de la columna items, una columna inpedendiente llamada *playtime_forever* la cual fue llevada a tipo *int* y con la cula se obtuvo una columna adiconal *playtime_hours* con valores llevados a horas apartir de los valores de esta primera.
El DF que se creo con el archivo games se realizo con  los datos de las columnas independientes especificamente las de genres. 


- userforgenre(género: str): Devuelve el top 5 de usuarios con más horas de juego en el género especificado, junto con su URL y user_id.

Para esta funcion utilizamos el DF realizado en la funcion anterior ya que contenia las columnas y datos necesdarias para aplicar esta funcion tambien.


- developer(desarrollador: str): Devuelve la cantidad de items y el porcentaje de contenido gratuito por año para la empresa desarrolladora especificada.

Aca utilizamos los datos del archivo games especificamente las columnas *'release_date','developer','price','items_count'* con las culaes se armo un nuevo DF el cual procedimos a limpar, los valores vacios se rellenaron con un randon de los valores encontrados para hacer el modelo mas eficiente, la columna de *items_count* se llevo a tipo inter y la columna *price* solo dejamos los valores que contenian la palabra *Free*. Luego procedimos a tomar una muestra mas chica de todo los datos originales. en la columna de *'release_date'* eliminas datos no concurrentes al tipo deseado.


Deployment
El proyecto se puedo implementar en un servicio de alojamiento web. Escogimos Railway para consumir la API desde la web.
proyectoindividualmljc-production.up.railway.app


Desarrollo de la API

Se debe implementar una API utilizando el framework FastAPI para exponer los datos y funcionalidades del proyecto. A continuación, se describen las funciones que deben implementarse como endpoints se utilizaran las funciones creadas anteriormente


Modelo de Aprendizaje Automático

El modelo que tomamos para ejecutar fue:

Sistema de Recomendación ítem-ítem
recomendacion_juego(id de producto): Recibe el ID de un juego y devuelve una lista con 5 juegos recomendados similares al ingresado.


Video de Presentación
enlance : 

Cómo Ejecutar el Proyecto
Clone este repositorio en su máquina local.

git clone https://github.com/jcchmd29/ProyectoIndividualML.JC


La API estará disponible en http://127.0.0.1:8000/docs#.


¡Gracias por ser parte de este emocionante proyecto! Si tiene alguna pregunta o necesita ayuda, no dude en ponerse en contacto con nosotros. ¡Esperamos ver sus contribuciones y resultados


