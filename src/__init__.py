from src.models.predict_model import predict_model
from fastapi import FastAPI

app = FastAPI()


@app.post("/predict")
async def predict(data_to_predict: dict):
    """
    Endpoint to make predictions using the trained model.

    Args:
        data_to_predict (dict): Input data for making predictions.

    Returns:
        dict: Predicted labels.
    """
    model_path = "models/ContentBasedFiltering.pkl"

    predictions = predict_model(model_path, data_to_predict)

    return predictions
