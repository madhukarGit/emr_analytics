
from util import get_spark_session
import os

def main():
  env = os.environ.get("Environ")
  spark = get_spark_session(env,"Analytics Activity")
  
  
  
if __name__ == '__main__':
  main()