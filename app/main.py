from fastapi import FastAPI
from app.model import train_and_save_model, load_model
from app.schemas import HouseFeatures, BatchPredictionRequest
from app.utils import convert_csv_to_batch_request
import numpy as np
import os

app = FastAPI(title="Housing Price Prediction API")

# Load or train model
if not os.path.exists("model/housing_model.pkl"):
    model, metrics, feature_names = train_and_save_model()
else:
    model, metrics, feature_names = load_model()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/model-info")
def model_info():
    return {
        "coefficients": dict(zip(feature_names, model.coef_)),
        "intercept": model.intercept_,
        "metrics": metrics
    }


@app.post("/predict")
def predict(data: HouseFeatures):
    features = np.array([list(data.dict().values())])
    prediction = model.predict(features)
    return {"predicted_price": prediction[0]}


@app.post("/predict-batch")
def predict_batch(data: BatchPredictionRequest):
    features = np.array([list(house.dict().values()) for house in data.houses])
    predictions = model.predict(features)
    return {"predicted_prices": predictions.tolist()}


@app.post("/predict-from-csv")
def predict_from_csv():
    payload = convert_csv_to_batch_request(
        "data/Test Data For Prediction.csv"
    )

    features = [list(house.values()) for house in payload["houses"]]
    predictions = model.predict(features)

    return {
        "total_records": len(predictions),
        "predicted_prices": predictions.tolist()
    }