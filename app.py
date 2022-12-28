
from util import get_spark_session
import os
from read import read_files
from process import transform
from write import to_files 

def main():
  env = os.environ.get("Environ")
  spark = get_spark_session(env,"Analytics Activity")
  df = read_files(spark)
  df_transformed = transform(df)
  tgt_dir="s3://ghvemractivitydata/write/"
  tgt_file_format="parquet"
  to_files(df_transformed,tgt_dir,tgt_file_format)
  
if __name__ == '__main__':
  main()