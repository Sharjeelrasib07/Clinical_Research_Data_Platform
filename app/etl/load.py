import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from app.utils.logger import get_logger

logger = get_logger(__name__)
load_dotenv()


def get_engine():
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_password = os.getenv("POSTGRES_PASSWORD", "postgres")
    db_host = os.getenv("POSTGRES_HOST", "localhost")
    db_port = os.getenv("POSTGRES_PORT", "5432")
    db_name = os.getenv("POSTGRES_DB", "research_db")

    database_url = (
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        f"?sslmode=require"
    )
    return create_engine(database_url)


def load_to_postgres(df, table_name: str):
    logger.info(f"Loading {len(df)} rows into table '{table_name}'")
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists="append", index=False)
    logger.info(f"Successfully loaded data into '{table_name}'")