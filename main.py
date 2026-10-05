from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="FraudShield AI")

class Transaction(BaseModel):
    amount: float
    location: str
    device: str

@app.get("/")
def home():
    return {"message": "Welcome to FraudShield AI"}

@app.post("/predict")
def predict(transaction: Transaction):
    # Placeholder logic — replace with ML model later
    risk_score = round(random.uniform(0, 1), 2)
    return {"risk_score": risk_score, "status": "fraud" if risk_score > 0.7 else "safe"}
