from fastapi import APIRouter
from app.models.ml_model import predict

router = APIRouter()

@router.post("/")
async def predict_endpoint(input_data: dict):
    prediction = predict(input_data)
    return prediction
