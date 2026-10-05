from fastapi import FastAPI

app = FastAPI(title="FraudShield AI")

@app.get("/")
def home():
    return {"message": "Welcome to FraudShield AI"}
