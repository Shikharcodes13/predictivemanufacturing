import shutil

from pathlib import Path

DATA_PATH = Path("app/data/uploaded_data.csv")

def save_file(file):
    with open(DATA_PATH, "wb") as f:
        shutil.copyfileobj(file.file, f)
