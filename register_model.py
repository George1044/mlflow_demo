import mlflow
import dagshub
# dagshub.init(repo_owner='George1044', repo_name='mlflow_demo', mlflow=True)

# Register the latest model to the model registry
experiment_name = "my_ml_experiment"
experiment = mlflow.get_experiment_by_name(experiment_name)
runs = mlflow.search_runs(experiment.experiment_id)
latest_run_id = runs.iloc[0].run_id

result = mlflow.register_model(
    model_uri=f"runs:/{latest_run_id}/random_forest_model",
    name="RandomForestModel"
)

print(f"Model registered: {result.name}, version: {result.version}")
