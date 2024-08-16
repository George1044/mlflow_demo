# MLFlow Demo
import dagshub
dagshub.init(repo_owner='George1044', repo_name='mlflow_demo', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


mlflow models serve -m "models:/RandomForestModel/1" -p 1234 --no-conda

export MLFLOW_TRACKING_URI='https://dagshub.com/George1044/mlflow_demo.mlflow'
mlflow models build-docker --name mlflow-demo --model-uri 'models:/RandomForestModel/1'