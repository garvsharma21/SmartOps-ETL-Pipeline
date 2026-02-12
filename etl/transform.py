import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)


def transform(input_path: str, output_path: str) -> str:
    input_path = Path(input_path)
    output_path = Path(output_path)

    df = pd.read_csv(input_path)

    # Drop missing rows
    df = df.dropna()

    # Example transformation: filter age > 18 if column exists
    if "age" in df.columns:
        df = df[df["age"] > 18]

    # Create output folder if not exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save transformed CSV
    df.to_csv(output_path, index=False)

    logger.info("Transformation complete → %s", output_path)

    return str(output_path)