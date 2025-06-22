from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("CSV to Parquet") \
    .getOrCreate()

# Load CSV using full path
df = spark.read.csv(r"C:\pyspark-clean\people.csv", header=True, inferSchema=True)

# Show data
df.show()

# Save as Parquet using full path
df.write.parquet(r"C:\pyspark-clean\output_parquet")

spark.stop()
