import json
from fastapi import APIRouter
from app.api.database import run_query

router = APIRouter()


@router.get("/stats/gender-distribution")
def gender_distribution():
    sex_query = """
        SELECT sex_at_birth, COUNT(*) AS count
        FROM patients
        GROUP BY sex_at_birth
        ORDER BY sex_at_birth
    """
    gender_query = """
        SELECT gender_identity, COUNT(*) AS count
        FROM patients
        GROUP BY gender_identity
        ORDER BY gender_identity
    """

    sex_results = run_query(sex_query)
    gender_results = run_query(gender_query)

    return {
        "sex_at_birth": {row["sex_at_birth"]: row["count"] for row in sex_results},
        "gender_identity": {row["gender_identity"]: row["count"] for row in gender_results},
    }


@router.get("/stats/diagnosis-summary")
def diagnosis_summary():
    query = """
        SELECT diagnosis_code, COUNT(*) AS count
        FROM patients
        GROUP BY diagnosis_code
        ORDER BY diagnosis_code
    """
    results = run_query(query)
    return {row["diagnosis_code"]: row["count"] for row in results}


@router.get("/stats/data-quality")
def get_data_quality():
    try:
        with open("reports/data_quality_report.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "metadata": {
                "last_etl_run": "Unavailable"
            },
            "patients": {
                "raw_records": 0,
                "cleaned_records": 0,
                "dropped_records": 0
            },
            "visits": {
                "raw_records": 0,
                "cleaned_records": 0,
                "dropped_records": 0
            },
            "lab_results": {
                "raw_records": 0,
                "cleaned_records": 0,
                "dropped_records": 0
            }
        }