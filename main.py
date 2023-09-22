from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
import pandas as pd
from textblob import TextBlob

# cargar Df para las funciones

# funcion 1
df_games_reviews = pd.read_csv('df_games_reviewsf1.csv')

# funcion 2
def_reviews_api2 = pd.read_csv('def_reviews_api2.csv')

# funcion 3
df3 = pd.read_csv('resultados_num.csv')

# funcion 4
df4 = pd.read_csv('df_final_api3y4.csv')

# funcion 5
df_gamesf5_free = pd.read_csv('df_gamesf5_free.csv')


app = FastAPI(title="Bienvenidos A mi primera API")


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=308)

@app.get("/")
def read_root():
    return {"Bienvenidos A mi primera API"}


@app.get('/userdata/{user_id}')
def userdata(User_id: str):
# Filtrar los datos para el usuario específico
    datos_usuario = df_games_reviews[df_games_reviews['user_id'] == User_id]
    
    # Calcular la cantidad de dinero gastado por el usuario
    total_gastado = df_games_reviews[df_games_reviews['user_id'] == User_id]['price'].sum()
    
    # Calcular el porcentaje de recomendación en base a la columna correcta (ajusta esto)
    # Suponiendo que "opiniones.recomendacion" es la columna relevante en df_original
    porcentaje_recomendacion = (datos_usuario['recommend'].sum() / len(datos_usuario)) * 100
    
    # Calcular la cantidad de ítems
    cantidad_items = df_games_reviews[df_games_reviews['user_id'] == User_id]['items_count'].sum()
    
    # Devolver los resultados como un diccionario
    resultados = {
        'id_usuario': User_id,
        'total_gastado': total_gastado,
        'porcentaje_recomendacion': porcentaje_recomendacion,
        'cantidad_items': cantidad_items
    }
    
    return resultados


@app.get('/countreviews/{fecha_inicio,fecha_fin}')
def countreviews(fecha_inicio: str, fecha_fin:str):
    # Filtrar el DataFrame por las fechas dadas
    df_filtrado = def_reviews_api2[(def_reviews_api2['fecha'] >= fecha_inicio) & (def_reviews_api2['fecha'] <= fecha_fin)]

    # Calcular la cantidad de usuarios únicos
    usuarios_unicos = df_filtrado['user_id'].nunique()

    # Calcular el porcentaje de recomendación promedio
    porcentaje_promedio = df_filtrado['recommend'].mean() * 100

    # Calcular la cantidad de items
    cantidad_items = len(df_filtrado)

    # Devolver los resultados como un diccionario
    resultados = {
        f'Cantidad de usuarios que realizaron reviews entre {fecha_inicio} y {fecha_fin}': usuarios_unicos,
        'Porcentaje de recomendación promedio': porcentaje_promedio,
        'Cantidad de items': cantidad_items
    }

    return resultados


@app.get('/genre/{genero}')
def genre(genero:str):
    # Filtra el DataFrame para quedarte solo con las filas donde el género tiene un valor mayor que 0
    df_genre = df3[df3[genero] > 0]

    # Ordena el DataFrame por la columna 'playtime_forever' de manera descendente
    df_sorted = df_genre.sort_values(by='playtime_forever', ascending=False)

    # Resetea el índice del DataFrame ordenado
    df_sorted.reset_index(drop=True, inplace=True)

    # Encuentra la posición del género en el DataFrame ordenado
    position = df_sorted[df_sorted[genero] > 0].index[0] + 1

    # Crear un diccionario con la respuesta
    response = {
    
        'Genero': genero,
        "position de ranking": position
    }

    return response

@app.get('/userforgenre/{género}')
def userforgenre(genero:str):
    # validar escritura
    genero = genero.title()

    # Filtrar el DataFrame original por el género especificado
    df_filtered = df4[df4[genero] == 1]

    if df_filtered.empty:
        return {"Mensaje": "No se encontraron datos para el género especificado."}

    # Ordenar el DataFrame filtrado por horas de juego en orden descendente
    df_sorted = df_filtered.sort_values(by='playtime_hours', ascending=False)

    # Tomar las primeras 5 filas (Top 5)
    top_5 = df_sorted.head(5)

    # Resetear el índice para mostrarlo en el resultado final
    top_5.reset_index(drop=True, inplace=True)

    # Seleccionar las columnas deseadas
    result = top_5[['user_id', 'user_url', 'playtime_hours', genero]]

    # Convertir el resultado en un diccionario
    result_dict = result.to_dict(orient='records')

    return result_dict

@app.get('/developer/{desarrollador}')
def developer( desarrollador : str ):
    # Filtrar el DataFrame para obtener solo las filas del desarrollador especificado
    df_filtrado = df_gamesf5_free[df_gamesf5_free['developer'] == desarrollador]
    
    # Calcular el porcentaje de contenido Free por año
    conteo_free_por_anio = df_filtrado[df_filtrado['price'].str.contains('Free', case=False)]
    conteo_free_por_anio = conteo_free_por_anio['year'].value_counts(normalize=True).reset_index()
    conteo_free_por_anio.columns = ['Año', 'Contenido Free']
    conteo_free_por_anio['Contenido Free'] = (conteo_free_por_anio['Contenido Free'] * 100).round(2).astype(str) + ' %'
    
    # Convertir el resultado en un diccionario
    result_dict = conteo_free_por_anio.to_dict(orient='records')
    
    return result_dict




