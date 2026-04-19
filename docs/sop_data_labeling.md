# Standard Operating Procedure (SOP)
## Data Labeling and Dataset Standardization

---

## 1. Purpose

This SOP defines the rules for labeling, organizing, and standardizing structured research datasets used in the platform.  
The objective is to ensure consistency, readability, and reproducibility across all patient, visit, and laboratory data.

---

## 2. Scope

This SOP applies to all datasets ingested into the platform, including:

- Patient records
- Visit records
- Laboratory results

All datasets are synthetic and pseudonymized.

---

## 3. Naming Conventions

### 3.1 File Naming
Raw and processed files should use clear, lowercase, underscore-separated names:

- `patients.csv`
- `visits.csv`
- `lab_results.csv`
- `patients_cleaned.csv`
- `visits_cleaned.csv`
- `lab_results_cleaned.csv`

### 3.2 Column Naming
Column names must:
- use lowercase letters
- use underscores instead of spaces
- avoid special characters
- remain semantically meaningful

Examples:
- `patient_id`
- `sex_at_birth`
- `gender_identity`
- `visit_date`

---

## 4. Labeling Standards

### 4.1 Patient Data
Required labels include:
- `patient_id`
- `sex_at_birth`
- `gender_identity`
- `age`
- `bmi`
- `diagnosis_code`
- `created_at`

### 4.2 Visit Data
Required labels include:
- `visit_id`
- `patient_id`
- `visit_date`
- `department`
- `blood_pressure_systolic`
- `blood_pressure_diastolic`
- `glucose_level`
- `physician_note_summary`

### 4.3 Laboratory Data
Required labels include:
- `result_id`
- `patient_id`
- `test_name`
- `test_value`
- `unit`
- `test_date`

---

## 5. Value Standardization

To maintain consistency:

- Dates must use ISO-style formatting (`YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS`)
- Numeric values must be stored in numeric fields
- Categorical fields must use predefined values where possible

Examples:
- `sex_at_birth`: `female`, `male`
- `gender_identity`: `woman`, `man`, `non-binary`

---

## 6. Data Quality Rules

Before loading into the database:

- duplicate identifiers must be removed
- required fields must not be null
- invalid data types must be corrected or excluded
- values outside expected ranges must be flagged

Examples:
- `age` must be between 0 and 120
- `bmi` must be numeric
- `test_value` must be numeric

---

## 7. Processed Data Output

After validation and labeling checks, cleaned files are stored in:

```text
data/processed/