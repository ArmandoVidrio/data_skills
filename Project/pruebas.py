import os
import pandas as pd
import json
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Cargar la clave API desde las variables de entorno
api_key = os.getenv('SERPAPI_API_KEY')

# Configurar los parámetros de búsqueda
params = {
    "engine": "google_jobs",
    "q": "Data Engineer",
    "location": "United States",
    "api_key": api_key
}

# Crear una instancia de GoogleSearch y realizar la búsqueda
# Inicializar variables
total_jobs = 0
page = 1

while True:
    # Crear una instancia de GoogleSearch y realizar la búsqueda
    search = GoogleSearch(params)
    results = search.get_dict()
    normalize_results = json.normalize(results)

    # Verificar la respuesta completa
    df = pd.DataFrame(normalize_results)
    print(df.headers)

    # Imprimir los resultados y contar los trabajos
    jobs = results.get('jobs_results', [])
    for job in jobs:
        print(job)
        total_jobs += 1

    print(f"Total jobs so far: {total_jobs}")

    # Verificar si hay un next_page_token
    next_page_token = results.get('next_page_token')
    if not next_page_token:
        break

    # Actualizar los parámetros de búsqueda con el next_page_token
    params['next_page_token'] = next_page_token
    page += 1

print(f"Total jobs: {total_jobs}")



