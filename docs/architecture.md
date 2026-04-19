# System Architecture

---

## 1. Overview

The platform follows a layered architecture to ensure separation of concerns, scalability, and reproducibility.

---

## 2. High-Level Flow
Raw Data (CSV)
↓
ETL Pipeline (Python + Pandas)
↓
Processed Data Layer
↓
PostgreSQL Database
↓
FastAPI Backend
↓
React Frontend

---

## 3. Components

### 3.1 Data Layer

- `data/raw/` → incoming datasets  
- `data/processed/` → cleaned and standardized data  

---

### 3.2 ETL Pipeline

Responsible for:

- extracting raw data
- validating datasets
- cleaning and transforming data
- loading into PostgreSQL

Modules:
- `extract.py`
- `transform.py`
- `load.py`
- `pipeline.py`

---

### 3.3 Database Layer

PostgreSQL database with structured schema:

Tables:
- `patients`
- `visits`
- `lab_results`

Key features:
- primary keys
- foreign key relationships
- structured data types

---

### 3.4 API Layer

FastAPI backend provides:

- data retrieval endpoints
- aggregated statistics
- health check endpoint

Example endpoints:
- `/patients`
- `/visits`
- `/labs`
- `/stats/*`

---

### 3.5 Frontend Layer

React-based dashboard:

- displays key metrics
- visualizes data using charts
- allows user interaction (search/filter)

---

### 3.6 Infrastructure Layer

Docker is used to:

- containerize services
- manage dependencies
- ensure reproducibility

Services include:
- database container
- application container

---

## 4. Design Principles

- modular architecture
- separation of concerns
- reproducibility via containerization
- clear data flow between layers

---

## 5. Future Enhancements

- monitoring (Prometheus / Grafana)
- CI/CD pipelines
- cloud deployment (Azure / OpenStack)
- scalable data ingestion

---

## 6. Summary

The architecture ensures that the platform is:

- structured
- scalable
- maintainable
- aligned with real-world data systems

---