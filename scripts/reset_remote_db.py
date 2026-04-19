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

with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE lab_results, visits, patients RESTART IDENTITY CASCADE;"))

print("Remote database tables cleared successfully.")