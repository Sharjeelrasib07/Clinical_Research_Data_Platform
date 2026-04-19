from fastapi import APIRouter
from app.api.database import run_query

router = APIRouter()

@router.get("/visits")
def get_visits():
    query = """
        SELECT visit_id, patient_id, visit_date, department,
               blood_pressure_systolic, blood_pressure_diastolic,
               glucose_level, physician_note_summary
        FROM visits
        ORDER BY visit_id
    """
    return run_query(query)