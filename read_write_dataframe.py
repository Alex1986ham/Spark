from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Our first Spark SQL example") \
    .getOrCreate()

spark.sparkContext.getConf().getAll()
