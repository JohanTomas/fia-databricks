# Databricks notebook source
# COMMAND ----------
# DBFS-style magia o Python directo
# CONEXIÓN 1: GitHub (Consumo de archivo CSV remoto)

import pandas as pd

url_github = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
print("Conectando a GitHub...")

df_github_pd = pd.read_csv(url_github)
df_github_spark = spark.createDataFrame(df_github_pd)

print("✅ Conexión 1 Exitosa: Datos cargados desde GitHub")
display(df_github_spark.limit(5))

# COMMAND ----------

# COMMAND ----------
# CONEXIÓN 2: API REST (Consumo de API HTTP externa)

import requests
import json

url_api = "https://api.github.com/users/JohanTomas"
print("Conectando a la API REST...")

response = requests.get(url_api)

if response.status_code == 200:
    data_json = response.json()
    # Convertimos el diccionario a un DataFrame de PySpark
    df_api = spark.read.json(sc.parallelize([json.dumps(data_json)]))
    print("✅ Conexión 2 Exitosa: Datos obtenidos de la API REST")
    display(df_api.select("login", "name", "public_repos", "followers", "created_at"))
else:
    print(f"Error al conectar con la API: {response.status_code}")

# COMMAND ----------

# COMMAND ----------
# CONEXIÓN 3: Google Drive / HTTP Direct Stream

import urllib.request

# Enlace de un archivo CSV público en Google Drive / Servidor remoto
url_drive = "https://kaggle.com" # O usa un CSV directo de Google Drive / Web público:
url_csv_publico = "https://gist.githubusercontent.com/netj/8836201/raw/6f930834fa3de72f84dd64f702b06825d7e0f49e/iris.csv"

local_path = "/tmp/datos_drive.csv"

print("Descargando archivo desde repositorio externo / Google Drive...")
urllib.request.urlretrieve(url_csv_publico, local_path)

df_drive_spark = spark.read.csv(f"file:{local_path}", header=True, inferSchema=True)

print("✅ Conexión 3 Exitosa: Archivo remoto leído correctamente")
display(df_drive_spark.limit(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Pipeline ejecutado correctamente desde GitHub Actions