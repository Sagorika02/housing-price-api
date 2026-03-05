# 🏠 Housing Price Prediction API

A containerized Machine Learning API built with **FastAPI** and **Scikit-learn** to predict housing prices based on property features.

---

## Features

- Linear Regression model  
- Predict prices (single & batch)  
- View model coefficients & metrics  
- Health check endpoint  
- Dockerized deployment  
- Swagger UI

---

## Dataset

Features:

- `square_footage`, `bedrooms`, `bathrooms`, `year_built`, `lot_size`, `distance_to_city_center`, `school_rating`  
Target: `price`  

`id` column excluded from training.

---

## Run Locally

1. Create virtual environment  
`python -m venv venv`

2. Activate virtual environment  

   Mac / Linux:
   `source venv/bin/activate`
   
   Windows:
   `venv\Scripts\activate`

3. Install dependencies  
`pip install -r requirements.txt`

4. Start server  
`uvicorn app.main:app --reload`

5. Swagger UI  
Open `http://127.0.0.1:8000/docs`

---

## Docker

1. Build image  
`docker build -t housing-api .`

2. Run container  
`docker run -p 8000:8000 housing-api`

---

## API Endpoints

1. ### Health Check
    **GET** `/health`  
    Returns API status.

2. ### Predict Price for a house
    **POST** `/predict`
    
    **Example request:**
    
    ```json
    {
        "square_footage": 1500,
        "bedrooms": 3,
        "bathrooms": 2,
        "year_built": 2000,
        "lot_size": 7000,
        "distance_to_city_center": 5,
        "school_rating": 8
    }
    ```
    **Example response:**
    
    ```json
    {
      "predicted_prices": 245000.32
    }
    ```

3. ### Predict Price for batch
    **POST** `/predict-batch`
    
    **Example request:**
    
    ```json
    [
      {
          "square_footage": 1500,
          "bedrooms": 3,
          "bathrooms": 2,
          "year_built": 2000,
          "lot_size": 7000,
          "distance_to_city_center": 5,
          "school_rating": 8
      },
      {...}
    ]
    ```
    **Example response:**
    
    ```json
    {
      "predicted_prices": [
        230283.12105624285,
        47707.56676927302
      ]
    }
    ```

4. ### Model Info
   **GET** `/model-info`  
   Returns model coefficients, intercept, R² score, and mean squared error.

5. ### Predict from csv file (Test Data For Prediction.csv)
   **POST** `/predict-from-csv`

   **Example respomse:**

   ```json
    {
      "total_records": 10,
      "predicted_prices": [
        258061.41487809923,
        366023.17274088226,
        170871.0338741634,
        302774.5705831442,
        212024.90248179715,
        419217.6661086632,
        264611.13953406084,
        148005.59859441128,
        351107.94192749634,
        191117.0516237868
      ]
    }
   ```
   




