from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("IcebergTest") \
    .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.my_catalog.catalog-impl", "org.apache.iceberg.hadoop.HadoopCatalog") \
    .config("spark.sql.catalog.my_catalog.warehouse", "s3a://my-bucket/warehouse") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()

data = [(1, "Alice"), (2, "Bob")]
df = spark.createDataFrame(data, ["id", "name"])

# Create Iceberg table inside database 'default'
df.writeTo("my_catalog.default.employees").createOrReplace()

print("Table created and data written successfully!")
spark.stop()
