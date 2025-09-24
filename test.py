import os
os.environ['PYSPARK_PYTHON'] = r"C:\Users\PHYNO ZEUS\switch\data-engineering-roadmap-2025\venv\Scripts\python.exe"
os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\PHYNO ZEUS\switch\data-engineering-roadmap-2025\venv\Scripts\python.exe"
os.environ['JAVA_HOME'] = r"C:\Program Files\Eclipse Adoptium\jdk-11.0.28.6-hotspot"
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("TestPySpark").getOrCreate()
print("✅ Spark Session Created")
