import mlflow

# Set the experiment name (create it if it doesn't exist)
mlflow.set_experiment("my_ml_experiment")

print(f"Experiment ID: {mlflow.get_experiment_by_name('my_ml_experiment').experiment_id}")
