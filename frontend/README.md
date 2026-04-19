# Pseudonymized Research Data Platform

A full-stack data platform designed to simulate modern clinical research data infrastructure.
This project demonstrates how pseudonymized patient-style data can be ingested, processed, stored, and explored using a scalable and modular architecture.

---

## 🚀 Project Overview

This platform replicates key components of data-driven medical research systems:

* Data ingestion and transformation using Python ETL pipelines
* Structured storage in PostgreSQL
* API access via FastAPI
* Interactive frontend dashboard using React
* Containerized environment using Docker

The system reflects real-world workflows in research environments, including secure handling of pseudonymized data and scalable data processing pipelines.

---

## 🏗️ Architecture

```
Raw Data (CSV)
      ↓
ETL Pipeline (Python + Pandas)
      ↓
Processed Data Layer
      ↓
PostgreSQL Database
      ↓
FastAPI Backend (REST APIs)
      ↓
React Frontend Dashboard
```

---

## ⚙️ Tech Stack

### Backend

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pandas

### Frontend

* React (Vite)
* Recharts

### Infrastructure

* Docker & Docker Compose

---

## 🔄 Data Pipeline (ETL)

The ETL pipeline performs:

* Extraction from raw CSV datasets
* Data validation and cleaning
* Transformation into structured formats
* Loading into PostgreSQL tables

The pipeline ensures:

* Removal of duplicates
* Schema validation
* Handling of missing values
* Consistent data formatting

---

## 📊 Features

### Dashboard

* Total patients, visits, and lab results
* API health status
* Gender distribution visualization
* Diagnosis summary chart

### Data Exploration

* Searchable patient table
* Visit records with filtering
* Lab results overview

### API Endpoints

* `/health`
* `/patients`
* `/visits`
* `/labs`
* `/stats/gender-distribution`
* `/stats/diagnosis-summary`

---

## 🔐 Data Privacy

All data used in this project is **synthetic and pseudonymized**.
No real patient information is included.

This project demonstrates:

* Secure data handling
* Pseudonymization practices
* Controlled access to structured datasets

---

## 🐳 Running the Project

### 1. Start Docker services

```bash
docker compose up --build
```

### 2. Run ETL pipeline

```bash
docker compose exec app python -m app.etl.pipeline
```

### 3. Start FastAPI backend

```bash
docker compose exec app uvicorn app.api.main:app --host 0.0.0.0 --port 8000
```

### 4. Start frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🌐 Access Points

* API Docs: http://localhost:8000/docs
* Frontend Dashboard: http://localhost:5173

---

## 🧪 Synthetic Data Generation

```bash
python scripts/generate_fake_data.py
```

Generates:

* Patient records
* Visit data
* Lab results

---
## 📌 Project Purpose

This project demonstrates practical skills in:

* Data engineering workflows
* API development
* Database design
* Full-stack integration
* Cloud-ready infrastructure
---

## 👤 Author

Sharjeel
Master’s Student – Geodesy & Geoinformation Science (TU Berlin)
