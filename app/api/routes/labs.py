from fastapi import APIRouter
from app.api.database import run_query

router = APIRouter()

@router.get("/labs")
def get_labs():
    query = """
        SELECT result_id, patient_id, test_name, test_value, unit, test_date
        FROM lab_results
        ORDER BY result_id
    """
    return run_query(query)