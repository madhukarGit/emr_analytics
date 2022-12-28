# emr_analytics
Elastic map reduce production ready code

# .env configuration
PYTHONPATH=/usr/lib/spark/python:/usr/lib/spark/python/py4j-0.10.9.5-src.zip

# run the spark appliction via s3 packaged zip python files and app.py in cluster mode
spark-submit --master yarn --deploy-mode cluster --conf "spark.yarn.appMasterEnv.Environ=PROD" --py-files  s3://emranalytics-backupcode-productionize/itvgithubdataAnalytics.zip s3://emranalytics-backupcode-productionize/app.py



# run the spark appliction via packaged zip python files and app.py in cluster mode
spark-submit --master yarn --deploy-mode cluster --conf "spark.yarn.appMasterEnv.Environ=PROD" --py-files itvgithubdataAnalytics.zip app.py

# run the spark appliction via packaged zip python files and app.py in client mode
spark-submit --master yarn --deploy-mode cluster --conf "spark.yarn.appMasterEnv.Environ=PROD" --py-files itvgithubdataAnalytics.zip app.py


# written files 

aws s3 rm s3://aws-emr-write-parquet-data --recursive