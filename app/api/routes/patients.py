from fastapi import APIRouter, HTTPException
from app.api.database import run_query

router = APIRouter()

@router.get("/patients")
def get_patients():
    query = """
        SELECT patient_id, sex_at_birth, gender_identity, age, bmi, diagnosis_code, created_at
        FROM patients
        ORDER BY patient_id
    """
    return run_query(query)

@router.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    query = """
        SELECT patient_id, sex_at_birth, gender_identity, age, bmi, diagnosis_code, created_at
        FROM patients
        WHERE patient_id = :patient_id
    """
    result = run_query(query, {"patient_id": patient_id})

    if not result:
        raise HTTPException(status_code=404, detail="Patient not found")

    return result[0]