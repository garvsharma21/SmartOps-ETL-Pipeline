import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

def load(input_path: str, output_path: str):
    input_path = Path(input_path)
    output_path = Path(output_path)

    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)

    # CLEANUP
    for f in ["extracted.csv", "transformed.csv"]:
        p = output_path.parent / f
        if p.exists():
            p.unlink()
