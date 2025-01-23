from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.models.ml_model import train_model, predict

# FastAPI instance
app = FastAPI()

# Define the input data model for prediction
class InputData(BaseModel):
    Temperature: float
    Run_Time: float

@app.on_event("startup")
def startup_event():
    """Train the model at the start of the application."""
    metrics = train_model()
    print(f"Training completed with metrics: {metrics}")

@app.post("/predict")
def get_prediction(input_data: InputData):
    """Predict downtime using the trained model."""
    result = predict(input_data.dict())
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result
