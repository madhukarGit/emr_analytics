
from util import get_spark_session
import os
from read import read_files
from process import transform
from write import to_files 

def main():
  env = os.environ.get("Environ")
  spark = get_spark_session(env,"Analytics Activity")
  read_file_json_s3="s3://ghvemractivitydata/analytics_sample.json"
  df = read_files(spark,read_file_json_s3)
  df_transformed = transform(df)
  tgt_dir="s3://ghvemractivitydata/write/"
  tgt_file_format="parquet"
  to_files(df_transformed,tgt_dir,tgt_file_format)
  df_transformed.limit(2).show()
  
if __name__ == '__main__':
  main()