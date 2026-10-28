
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentData(BaseModel):
    attendance: float
    internal_marks: float
    study_hours: float
    previous_marks: float

@app.get("/")
def home():
    return {"message": "Student Performance API is running"}

@app.post("/predict")
def predict(data: StudentData):
    score = (
        data.attendance * 0.30
        + data.internal_marks * 0.25
        + min(data.study_hours / 12, 1) * 100 * 0.15
        + data.previous_marks * 0.30
    )

    if score >= 75:
        result = "Good"
    elif score >= 50:
        result = "Average"
    else:
        result = "Poor"

    return {"prediction": result}
