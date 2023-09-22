# Proyecto de Análisis de Datos y Sistema de Recomendación

Este proyecto tiene como objetivo principal realizar un análisis de datos en un conjunto de datos relacionado con reseñas de juegos y desarrollar un sistema de recomendación basado en este análisis, construir un API y un Modelo Machine Learning. 

A continuación, se detallan los pasos y requerimientos para llevar a cabo este proyecto.

## Transformaciones de Datos y Análisis Exploratorio de los Datos (EDA)

En esta fase inicial del proyecto, se debe realizar un análisis exploratorio de los datos para investigar las relaciones entre las variables del conjunto de datos y si se requiere realizar transformaciones de datos. Sin embargo, se debe garantizar que el conjunto de datos se lea con el formato correcto y se pueden eliminar columnas innecesarias o solo trabajar con aquellas columnas que nos permitan optimizar el rendimiento de la API y el entrenamiento del modelo. **Esto ultimo fue lo que se decidio realizar**.

Luego de visualizar los datos en los 3 archivos dados (cabe resaltar que fueron de tipo **JSON** y pueden ser encontrados en el siguiente enlace https://drive.google.com/drive/folders/11-QXtPVj0q3Uds45IOByNn7jreSHuBtg?usp=drive_link ), se procedio a crear DF independiente a partir de las columnas que nos interesaban en cada uno de ellos para realizar las funciones solicitadas y guarados commo archivos **CSV** que hacen mas facil su manipulacion y de menos espacio en memeoria.

### A continuacion detallo cada funcion y la estructura de datos que se usaron para su armado.


userdata(User_id: str): Devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a las reseñas y la cantidad de items.

Para esta funcion utilizamos el archivo de items ali extrajimos datos de columnas anidadas las cuales desanidamos y le dimos el formato necesario hazta crear un DF limpio de este. Tambien usamos parte del archivo games, de la columna reviews que se encontraba anidada y luego de desanidar se procedio a  transformar esos datos en columnas separadas, utilizamos una de esas columnas independiente llamada price para obtener el costo de los gastos la cual concatenemos al DF de items limpio previamente obtenido.

countreviews(YYYY-MM-DD y YYYY-MM-DD: str): Devuelve la cantidad de usuarios que realizaron reseñas entre las fechas proporcionadas y el porcentaje de recomendación basado en las reseñas.

Para esta funcion utilizamos el archivo de items de la columa de su mismo nombre que previamente desanidamos y que obtenimos columnas independientes alli encontramos una columna llan¡mada posted. En dicha columna se encontraban los datos con las fechas que debiamos utilizar para esta funcion la cual debios dar formato solicitado. para ello eliminamos parte del valor inicial del dato como era la palabra *posted*, luego separamos cada parte de la fecha en columnas diferentes para poder aplicar algunas mejoras como llevar el valor de los meses de letras a numeros, los dias en formato de dos numeros y alli nos percatamos que le año tenia valores faltantes que procedimos a rellenar con la moda obrtenida del conjunto de datos existentes para el año. Tambien de las columnas independientes utilizamos la columna recommend la cual llevamos de valores booleanos a numericos donde True es 1 y False es 0.


genre(género: str): Devuelve la posición en la que se encuentra un género en el ranking de géneros, analizado bajo la columna 'PlayTimeForever'.

Aca utilizamos Df del archivos items y Df del archivos games, que luefo fueron unidos con un *inner join* por la columna user_id que ambos compartian  para obtener los datos de genero de juego.
El DF que se construyo del archivo items fue obtenido del DF desanidado previamente de la columna items, una columna inpedendiente llamada *playtime_forever* la cual fue llevada a tipo *int* y con la cula se obtuvo una columna adiconal *playtime_hours* con valores llevados a horas apartir de los valores de esta primera.
El DF que se creo con el archivo games se realizo con  los datos de las columnas independientes 


userforgenre(género: str): Devuelve el top 5 de usuarios con más horas de juego en el género especificado, junto con su URL y user_id.
Utilizamos el archivo games para crear un DF con los valores y columnas requeridas para esta funcion. El Df resultante lo armamos con las columnas app_name, user_id


developer(desarrollador: str): Devuelve la cantidad de items y el porcentaje de contenido gratuito por año para la empresa desarrolladora especificada.

sentiment_analysis(año: int): Devuelve una lista con la cantidad de registros de reseñas de usuarios categorizados con análisis de sentimiento para un año de lanzamiento dado.

Deployment
El proyecto se puede implementar en un servicio de alojamiento web como Render, Railway o cualquier otro que permita consumir la API desde la web.



Feature Engineering

Se debe crear una nueva columna llamada 'sentiment_analysis' en el conjunto de datos de reseñas de usuarios. Esta columna se llenará mediante análisis de sentimiento con NLP y tendrá los siguientes valores:

'0' si la reseña es negativa.
'1' si la reseña es neutral.
'2' si la reseña es positiva.
Si no es posible realizar el análisis de sentimiento debido a la falta de una reseña escrita, la columna 'sentiment_analysis' debe tomar el valor '1'.

Desarrollo de la API
Se debe implementar una API utilizando el framework FastAPI para exponer los datos y funcionalidades del proyecto. A continuación, se describen las funciones que deben implementarse como endpoints:

Modelo de Aprendizaje Automático
Se debe entrenar un modelo de recomendación, que puede ser de tipo ítem-ítem o user-item, o ambos si se desea. El modelo debe estar integrado en la API y tener la capacidad de proporcionar recomendaciones en función de la entrada del usuario.

Sistema de Recomendación ítem-ítem
recomendacion_juego(id de producto): Recibe el ID de un juego y devuelve una lista con 5 juegos recomendados similares al ingresado.
Sistema de Recomendación user-item
recomendacion_usuario(id de usuario): Recibe el ID de un usuario y devuelve una lista con 5 juegos recomendados para dicho usuario.
Video de Presentación
Se debe crear un video de presentación que muestre los resultados de las consultas propuestas y el funcionamiento del modelo de aprendizaje automático entrenado. El video debe incluir una breve introducción sobre el proyecto y lo que se mostrará en el video.

Cómo Ejecutar el Proyecto
Clone este repositorio en su máquina local.
bash
Copy code
git clone https://github.com/tuusuario/proyecto-analisis-recomendacion.git
Instale las dependencias necesarias.
bash
Copy code
pip install -r requirements.txt
Ejecute la aplicación.
bash
Copy code
python app.py
La API estará disponible en http://localhost:8000.

Contribuciones
Si desea contribuir a este proyecto, abra un problema o envíe una solicitud de extracción con sus sugerencias.

Licencia
Este proyecto está bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

¡Gracias por ser parte de este emocionante proyecto! Si tiene alguna pregunta o necesita ayuda, no dude en ponerse en contacto con nosotros. ¡Esperamos ver sus contribuciones y resultados


