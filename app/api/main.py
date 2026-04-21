from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.database import run_query
from app.api.routes import patients, visits, labs, stats, admin

app = FastAPI(
    title="Clinical Research Data Platform",
    description="API for accessing pseudonymized clinical-style research data",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://clinical-research-data-platform.vercel.app",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    try:
        run_query("SELECT 1")
        return {
            "status": "ok",
            "service": "clinical-research-data-platform",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "error",
            "service": "clinical-research-data-platform",
            "database": "not connected",
            "detail": str(e)
        }

app.include_router(patients.router)
app.include_router(visits.router)
app.include_router(labs.router)
app.include_router(stats.router)
app.include_router(admin.router)