from fastapi import APIRouter
from app.etl.pipeline import run_pipeline

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/run-etl")
def run_etl():
    try:
        result = run_pipeline()
        return {
            "status": "success",
            "message": result["message"],
            "stats": result["stats"],
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }