import pandas as pd
from app.utils.logger import get_logger

logger = get_logger(__name__)


def extract_csv(file_path: str) -> pd.DataFrame:
    logger.info(f"Extracting data from {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"Extracted {len(df)} rows from {file_path}")
    return df