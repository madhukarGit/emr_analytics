

def read_files(spark):
  df = spark. \
    read. \
      format('json') .\
        load("/Users/hmadhukar/Documents/Pyspark_load_json_pract/2022-01-03-1.json")
  return df