import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

def transform(input_path: str, output_path: str) -> str:
    input_path = Path(input_path)
    output_path = Path(output_path)

    df = pd.read_csv(input_path)

    df = df.dropna()

    if "age" not in df.columns:
        raise ValueError("Column 'age' not found")

    df = df[df["age"] > 18]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.info("Transformed %d rows to %s", len(df), output_path)
    return str(output_path)
