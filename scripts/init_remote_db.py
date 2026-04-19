import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    f"?sslmode=require"
)

engine = create_engine(DATABASE_URL)

schema_sql = """
CREATE TABLE IF NOT EXISTS patients (
    patient_id VARCHAR(64) PRIMARY KEY,
    sex_at_birth VARCHAR(20) NOT NULL,
    gender_identity VARCHAR(50),
    age INTEGER NOT NULL CHECK (age >= 0 AND age <= 120),
    bmi NUMERIC(5,2),
    diagnosis_code VARCHAR(20),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS visits (
    visit_id VARCHAR(64) PRIMARY KEY,
    patient_id VARCHAR(64) NOT NULL,
    visit_date DATE NOT NULL,
    department VARCHAR(100),
    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,
    glucose_level NUMERIC(6,2),
    physician_note_summary TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS lab_results (
    result_id VARCHAR(64) PRIMARY KEY,
    patient_id VARCHAR(64) NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    test_value NUMERIC(10,2) NOT NULL,
    unit VARCHAR(20),
    test_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);
"""

with engine.begin() as conn:
    for statement in schema_sql.strip().split(";"):
        stmt = statement.strip()
        if stmt:
            conn.execute(text(stmt))

print("Remote database schema initialized successfully.")