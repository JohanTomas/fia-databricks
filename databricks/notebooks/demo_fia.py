# Databricks notebook source
# MAGIC %md
# MAGIC # Demo FIA - Fundamentos de Inteligencia Artificial
# MAGIC ### Integración GitHub + Databricks

# COMMAND ----------

print("✅ Conexión exitosa entre GitHub y Databricks")
print("Autor: johan.malasquezvallegrande.edu.pe")

# COMMAND ----------

# Mostrar información del entorno
import sys
print(f"Python version: {sys.version}")

# COMMAND ----------

# Ejemplo de lectura de datos
data = [
    {"nombre": "Dataset 1", "registros": 1000},
    {"nombre": "Dataset 2", "registros": 2500},
    {"nombre": "Dataset 3", "registros": 500},
]

for item in data:
    print(f"📊 {item['nombre']}: {item['registros']} registros")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Pipeline ejecutado correctamente desde GitHub Actions