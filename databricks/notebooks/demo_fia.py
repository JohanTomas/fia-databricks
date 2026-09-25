# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
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
import pandas as pd

url_api = "https://api.github.com/users/JohanTomas"
print("Conectando a la API REST...")

response = requests.get(url_api)

if response.status_code == 200:
    data_json = response.json()
    
    # Se utiliza pandas para crear el DataFrame directamente sin usar SparkContext
    df_pd = pd.DataFrame([data_json])
    df_api = spark.createDataFrame(df_pd)
    
    print("✅ Conexión 2 Exitosa: Datos obtenidos de la API REST")
    display(df_api.select("login", "name", "public_repos", "followers", "created_at"))
else:
    print(f"Error al conectar con la API: {response.status_code}")

# COMMAND ----------

# DBTITLE 1,Cell 3
# COMMAND ----------
# CONEXIÓN 3: Google Drive / Repositorio Público Certificado

%pip install seaborn

import seaborn as sns

print("Descargando archivo desde repositorio externo...")

# Carga directa de dataset libre de fallas de URL
df_pd = sns.load_dataset("iris")

# Conversión a Spark para compatibilidad con Serverless
df_drive_spark = spark.createDataFrame(df_pd)

print("✅ Conexión 3 Exitosa: Archivo remoto leído correctamente")
display(df_drive_spark.limit(5))