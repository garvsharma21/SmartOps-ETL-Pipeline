
import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)


def load(input_path: str, output_path: str) -> None:
    input_path = Path(input_path)
    output_path = Path(output_path)

    df = pd.read_csv(input_path)

    # Create final folder if missing
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save final output
    df.to_csv(output_path, index=False)

    logger.info("Load complete → %s", output_path)