# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,expr

stockData = spark.sql(f"select * from stock_data")
stockData.printSchema()
print(stockData.columns)
display(stockData)


# COMMAND ----------

stockData = stockData.withColumnRenamed(" Ticker","Ticker")
#filter data based on ticker
GoogleStockData = stockData.filter(stockData.Ticker == "GOOGL")
display(GoogleStockData)

# COMMAND ----------



# Create a new column 'mean_price' in the DataFrame
GoogleStockData = GoogleStockData.withColumn(
    "Mean Price",
    (col("Open price") + col("Close price") + col("High price") + col("Low price")) / 4
)

# Show the result
display(GoogleStockData.select("Date","Mean Price"))

