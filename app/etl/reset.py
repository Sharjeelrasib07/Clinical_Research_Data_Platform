from sqlalchemy import text
from app.etl.load import get_engine
from app.utils.logger import get_logger

logger = get_logger(__name__)


def reset_tables():
    logger.info("Resetting database tables before ETL run")
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(
            text("TRUNCATE TABLE lab_results, visits, patients RESTART IDENTITY CASCADE;")
        )

    logger.info("Database tables reset successfully")