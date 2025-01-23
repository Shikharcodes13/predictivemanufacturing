from fastapi import APIRouter
from app.models.ml_model import train_model

router = APIRouter()

@router.post("/")
async def train_model_endpoint():
    metrics = train_model()
    return {"message": "Model trained successfully", "metrics": metrics}
