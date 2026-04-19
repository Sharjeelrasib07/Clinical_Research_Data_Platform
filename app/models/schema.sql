CREATE TABLE patients (
    patient_id VARCHAR(64) PRIMARY KEY,
    sex_at_birth VARCHAR(20) NOT NULL,
    gender_identity VARCHAR(50),
    age INTEGER NOT NULL CHECK (age >= 0 AND age <= 120),
    bmi NUMERIC(5,2),
    diagnosis_code VARCHAR(20),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE visits (
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

CREATE TABLE lab_results (
    result_id VARCHAR(64) PRIMARY KEY,
    patient_id VARCHAR(64) NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    test_value NUMERIC(10,2) NOT NULL,
    unit VARCHAR(20),
    test_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);