

def read_files(spark,load_file):
  print("load file ",load_file)
  df = spark.read.format('json').load(load_file)
  return df