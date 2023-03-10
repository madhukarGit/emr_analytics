from pyspark.sql import SparkSession

def get_spark_session(env="Dev",appName="DataAnalytics"):
  if env == 'Dev':
    spark = SparkSession. \
      builder. \
        master('local'). \
          appName(appName). \
            getOrCreate()
    return spark
  if env == 'PROD':
    spark = SparkSession. \
      builder. \
        master('yarn'). \
          appName(appName). \
            getOrCreate()
    return spark
  return
          