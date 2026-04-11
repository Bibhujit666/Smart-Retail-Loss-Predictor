from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# ✅ Load models
regressor = joblib.load("regressor.pkl")
classifier = joblib.load("classifier.pkl")

@app.get("/")
def home():
    return {"message": "Retail Predictor API is running 🚀"}

@app.post("/predict")
def predict(data: dict):
    try:
        features = np.array([[
            data["temperature"],
            data["humidity"],
            data["footfall"],
            data["staff"],
            data["experience"],
            data["cold_chain"],
            data["is_weekend"]
        ]])

        # ✅ Predict loss
        loss = regressor.predict(features)[0]

        # ✅ Predict risk
        risk_val = classifier.predict(features)[0]
        risk = "High Risk" if risk_val == 1 else "Low Risk"

        return {
            "prediction": float(loss),
            "risk": risk
        }

    except Exception as e:
        return {"error": str(e)}