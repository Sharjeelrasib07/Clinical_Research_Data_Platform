import csv
import os
import random
from datetime import datetime, timedelta

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

NUM_PATIENTS = 60
NUM_VISITS = 120
NUM_LABS = 180

SEX_AT_BIRTH_OPTIONS = ["female", "male"]
GENDER_IDENTITY_OPTIONS = ["woman", "man", "non-binary"]
DIAGNOSIS_CODES = ["E11", "I10", "E66", "R53", "E78"]
DEPARTMENTS = [
    "Endocrinology",
    "Cardiology",
    "Internal Medicine",
    "Neurology",
    "General Practice",
]
LAB_TESTS = [
    ("HbA1c", "%"),
    ("LDL Cholesterol", "mg/dL"),
    ("Creatinine", "mg/dL"),
    ("Glucose", "mg/dL"),
    ("Triglycerides", "mg/dL"),
]

BASE_DATE = datetime(2026, 4, 1, 8, 0, 0)


def random_created_at(index: int) -> str:
    dt = BASE_DATE + timedelta(minutes=index * 17)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def random_visit_date() -> str:
    dt = BASE_DATE + timedelta(days=random.randint(0, 45))
    return dt.strftime("%Y-%m-%d")


def random_test_date() -> str:
    dt = BASE_DATE + timedelta(days=random.randint(0, 45))
    return dt.strftime("%Y-%m-%d")


def generate_patients():
    patients = []

    for i in range(1, NUM_PATIENTS + 1):
        patient_id = f"P{i:03d}"
        sex_at_birth = random.choice(SEX_AT_BIRTH_OPTIONS)

        if sex_at_birth == "female":
            gender_identity = random.choices(
                ["woman", "non-binary"], weights=[0.85, 0.15], k=1
            )[0]
        else:
            gender_identity = random.choices(
                ["man", "non-binary"], weights=[0.85, 0.15], k=1
            )[0]

        age = random.randint(18, 80)
        bmi = round(random.uniform(18.0, 35.0), 1)
        diagnosis_code = random.choice(DIAGNOSIS_CODES)
        created_at = random_created_at(i)

        patients.append(
            {
                "patient_id": patient_id,
                "sex_at_birth": sex_at_birth,
                "gender_identity": gender_identity,
                "age": age,
                "bmi": bmi,
                "diagnosis_code": diagnosis_code,
                "created_at": created_at,
            }
        )

    return patients


def generate_visits(patients):
    visits = []

    for i in range(1, NUM_VISITS + 1):
        visit_id = f"V{i:03d}"
        patient = random.choice(patients)
        patient_id = patient["patient_id"]
        department = random.choice(DEPARTMENTS)

        systolic = random.randint(105, 160)
        diastolic = random.randint(65, 100)
        glucose = round(random.uniform(85.0, 160.0), 1)

        notes = random.choice(
            [
                "Routine follow-up with stable condition.",
                "Patient reports fatigue and mild dizziness.",
                "Elevated blood pressure noted during consultation.",
                "Medication review recommended.",
                "Monitoring metabolic indicators over time.",
            ]
        )

        visits.append(
            {
                "visit_id": visit_id,
                "patient_id": patient_id,
                "visit_date": random_visit_date(),
                "department": department,
                "blood_pressure_systolic": systolic,
                "blood_pressure_diastolic": diastolic,
                "glucose_level": glucose,
                "physician_note_summary": notes,
            }
        )

    return visits


def generate_lab_results(patients):
    lab_results = []

    for i in range(1, NUM_LABS + 1):
        result_id = f"L{i:03d}"
        patient = random.choice(patients)
        patient_id = patient["patient_id"]
        test_name, unit = random.choice(LAB_TESTS)

        if test_name == "HbA1c":
            test_value = round(random.uniform(4.8, 8.5), 1)
        elif test_name == "LDL Cholesterol":
            test_value = round(random.uniform(70, 190), 1)
        elif test_name == "Creatinine":
            test_value = round(random.uniform(0.6, 1.5), 2)
        elif test_name == "Glucose":
            test_value = round(random.uniform(80, 180), 1)
        else:
            test_value = round(random.uniform(80, 250), 1)

        lab_results.append(
            {
                "result_id": result_id,
                "patient_id": patient_id,
                "test_name": test_name,
                "test_value": test_value,
                "unit": unit,
                "test_date": random_test_date(),
            }
        )

    return lab_results


def write_csv(file_path, fieldnames, rows):
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    random.seed(42)

    patients = generate_patients()
    visits = generate_visits(patients)
    lab_results = generate_lab_results(patients)

    write_csv(
        os.path.join(RAW_DIR, "patients.csv"),
        [
            "patient_id",
            "sex_at_birth",
            "gender_identity",
            "age",
            "bmi",
            "diagnosis_code",
            "created_at",
        ],
        patients,
    )

    write_csv(
        os.path.join(RAW_DIR, "visits.csv"),
        [
            "visit_id",
            "patient_id",
            "visit_date",
            "department",
            "blood_pressure_systolic",
            "blood_pressure_diastolic",
            "glucose_level",
            "physician_note_summary",
        ],
        visits,
    )

    write_csv(
        os.path.join(RAW_DIR, "lab_results.csv"),
        [
            "result_id",
            "patient_id",
            "test_name",
            "test_value",
            "unit",
            "test_date",
        ],
        lab_results,
    )

    print("Synthetic data generated successfully.")
    print(f"Patients: {len(patients)}")
    print(f"Visits: {len(visits)}")
    print(f"Lab Results: {len(lab_results)}")


if __name__ == "__main__":
    main()