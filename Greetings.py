from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[*]").getOrCreate()
    df = spark.read.csv("/work/DataScience/311_Cases.csv")
    print(df.count())