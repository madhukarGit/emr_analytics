from pyspark.sql import SparkSession

def get_spark_session(env,appName):
  if env == 'DEV':
    spark = SparkSession. \
      builder. \
        master('local'). \
          appName(appName). \
            getOrCreate()
    return spark
  return
          