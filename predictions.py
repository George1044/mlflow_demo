import requests

# Define the input data according to the MLflow format
data = {
    "dataframe_records": [
        {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    ]
}

# Make a POST request to the model server
response = requests.post("http://127.0.0.1:1234/invocations", json=data)

# Print the response from the model server
print(f"Prediction: {response.json()}")
