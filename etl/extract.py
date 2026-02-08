import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

def extract(input_path: str, output_path: str):
    logger.info("Starting extraction from %s", input_path)

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.info(
        "Extraction complete. Rows=%d, Columns=%d, Written to %s",
        df.shape[0], df.shape[1], output_path
    )

    return str(output_path)