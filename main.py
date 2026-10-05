from fastapi import FastAPI
from pydantic import BaseModel
import random
import joblib

app = FastAPI(title="FraudShield AI")

# Define the input schema
class Transaction(BaseModel):
    amount: float
    location: str
    device: str

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to FraudShield AI"}

# Health check route
@app.get("/health")
def health_check():
    return {"status": "running", "version": "1.0"}

# Load model (optional: replace with your trained scikit-learn model)
# For now, this is commented out until you train and save model.pkl
# model = joblib.load("model.pkl")

# Predict route
@app.post("/predict")
def predict(transaction: Transaction):
    # Placeholder logic: random risk score
    # Replace with: risk_score = model.predict_proba([[transaction.amount]])[0][1]
    risk_score = round(random.uniform(0, 1), 2)
    return {
        "risk_score": risk_score,
        "status": "fraud" if risk_score > 0.7 else "safe",
        "transaction": transaction.dict()
    }
