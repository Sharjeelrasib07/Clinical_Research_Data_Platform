import os
import pandas as pd
from app.utils.logger import get_logger
from app.utils.validation import (
    validate_patients,
    validate_visits,
    validate_lab_results,
)

logger = get_logger(__name__)

PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)


def transform_patients(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming patients data")
    df.columns = [col.strip().lower() for col in df.columns]
    df = validate_patients(df)
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df = df[df["created_at"].notna()]
    output_path = os.path.join(PROCESSED_DIR, "patients_cleaned.csv")
    df.to_csv(output_path, index=False)
    logger.info(f"Saved cleaned patients data to {output_path}")
    return df


def transform_visits(df: pd.DataFrame, valid_patient_ids: set) -> pd.DataFrame:
    logger.info("Transforming visits data")
    df.columns = [col.strip().lower() for col in df.columns]
    df = validate_visits(df, valid_patient_ids)
    output_path = os.path.join(PROCESSED_DIR, "visits_cleaned.csv")
    df.to_csv(output_path, index=False)
    logger.info(f"Saved cleaned visits data to {output_path}")
    return df


def transform_lab_results(df: pd.DataFrame, valid_patient_ids: set) -> pd.DataFrame:
    logger.info("Transforming lab results data")
    df.columns = [col.strip().lower() for col in df.columns]
    df = validate_lab_results(df, valid_patient_ids)
    output_path = os.path.join(PROCESSED_DIR, "lab_results_cleaned.csv")
    df.to_csv(output_path, index=False)
    logger.info(f"Saved cleaned lab results data to {output_path}")
    return df