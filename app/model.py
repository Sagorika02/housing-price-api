import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import joblib
import os

MODEL_PATH = "model/housing_model.pkl"

def train_and_save_model():
    df = pd.read_csv("data/House Price Dataset.csv")

    X = df.drop(["id", "price"], axis=1)
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "r2_score": r2_score(y_test, y_pred),
        "mse": mean_squared_error(y_test, y_pred)
    }

    os.makedirs("model", exist_ok=True)
    joblib.dump((model, metrics, X.columns.tolist()), MODEL_PATH)

    return model, metrics, X.columns.tolist()


def load_model():
    return joblib.load(MODEL_PATH)