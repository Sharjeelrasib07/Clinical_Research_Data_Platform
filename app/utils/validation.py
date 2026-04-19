import pandas as pd


def validate_patients(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["patient_id"])
    df = df[df["patient_id"].notna()]
    df = df[df["sex_at_birth"].notna()]
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df = df[df["age"].between(0, 120, inclusive="both")]
    df["bmi"] = pd.to_numeric(df["bmi"], errors="coerce")
    return df


def validate_visits(df: pd.DataFrame, valid_patient_ids: set) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["visit_id"])
    df = df[df["visit_id"].notna()]
    df = df[df["patient_id"].isin(valid_patient_ids)]
    df["visit_date"] = pd.to_datetime(df["visit_date"], errors="coerce")
    df = df[df["visit_date"].notna()]
    df["blood_pressure_systolic"] = pd.to_numeric(df["blood_pressure_systolic"], errors="coerce")
    df["blood_pressure_diastolic"] = pd.to_numeric(df["blood_pressure_diastolic"], errors="coerce")
    df["glucose_level"] = pd.to_numeric(df["glucose_level"], errors="coerce")
    return df


def validate_lab_results(df: pd.DataFrame, valid_patient_ids: set) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["result_id"])
    df = df[df["result_id"].notna()]
    df = df[df["patient_id"].isin(valid_patient_ids)]
    df["test_value"] = pd.to_numeric(df["test_value"], errors="coerce")
    df = df[df["test_value"].notna()]
    df["test_date"] = pd.to_datetime(df["test_date"], errors="coerce")
    df = df[df["test_date"].notna()]
    return df