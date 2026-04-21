from app.utils.data_quality import generate_report
from app.etl.extract import extract_csv
from app.etl.transform import (
    transform_patients,
    transform_visits,
    transform_lab_results,
)
from app.etl.load import load_to_postgres
from app.etl.reset import reset_tables
from app.utils.logger import get_logger

logger = get_logger(__name__)


def run_pipeline():
    logger.info("Starting ETL pipeline")

    stats = {}

    reset_tables()

    patients_raw = extract_csv("data/raw/patients.csv")
    patients_clean = transform_patients(patients_raw)
    load_to_postgres(patients_clean, "patients")

    stats["patients"] = {
        "raw_records": len(patients_raw),
        "cleaned_records": len(patients_clean),
        "dropped_records": len(patients_raw) - len(patients_clean),
    }

    valid_patient_ids = set(patients_clean["patient_id"].tolist())

    visits_raw = extract_csv("data/raw/visits.csv")
    visits_clean = transform_visits(visits_raw, valid_patient_ids)
    load_to_postgres(visits_clean, "visits")

    stats["visits"] = {
        "raw_records": len(visits_raw),
        "cleaned_records": len(visits_clean),
        "dropped_records": len(visits_raw) - len(visits_clean),
    }

    labs_raw = extract_csv("data/raw/lab_results.csv")
    labs_clean = transform_lab_results(labs_raw, valid_patient_ids)
    load_to_postgres(labs_clean, "lab_results")

    stats["lab_results"] = {
        "raw_records": len(labs_raw),
        "cleaned_records": len(labs_clean),
        "dropped_records": len(labs_raw) - len(labs_clean),
    }

    generate_report(stats)

    logger.info("ETL pipeline completed successfully")
    return {"message": "ETL pipeline completed successfully", "stats": stats}


if __name__ == "__main__":
    run_pipeline()