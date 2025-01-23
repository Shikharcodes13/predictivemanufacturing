from fastapi import APIRouter, UploadFile, HTTPException
from app.utils.file_handler import save_file

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")
    
    save_file(file)
    return {"message": f"{file.filename} uploaded successfully."}
