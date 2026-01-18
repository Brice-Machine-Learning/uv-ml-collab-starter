""" 
Download the UCI Adult (Census Income) dataset into data/raw.
-------------------------------------------------------------

The dataset is intentionally left unmodified to preserve
raw input fidelity for later cleaning and preprocessing steps.
"""

from pathlib import Path
import requests

DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
)

RAW_DATA_DIR = Path("data/raw/adult")
OUTPUT_FILE = RAW_DATA_DIR / "adult.data"
README_FILE = RAW_DATA_DIR / "README.md"


def download_dataset() -> None:
    """
    Download the UCI Adult (Census Income) dataset into data/raw.

    The dataset is intentionally left unmodified to preserve
    raw input fidelity for later cleaning and preprocessing steps.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    if OUTPUT_FILE.exists():
        print("Raw dataset already exists — skipping download.")
        return

    print("Downloading dataset...")
    response = requests.get(DATA_URL, timeout=30)
    response.raise_for_status()

    OUTPUT_FILE.write_text(response.text)
    print(f"Saved dataset to {OUTPUT_FILE}")

    _write_readme()
    print("Wrote dataset README.")


def _write_readme() -> None:
    README_FILE.write_text(
"""# Adult Census Income Dataset (Raw)

Source:
UCI Machine Learning Repository

Original URL:
https://archive.ics.uci.edu/ml/datasets/Adult

Notes:
- This file is intentionally stored in its original, raw form
- Missing values are represented as '?'
- Fields contain inconsistent whitespace
- No header row is included
- Data should NOT be modified in-place

All cleaning and preprocessing should be performed on a copy of this data
and written to data/processed/.
"""
    )



if __name__ == "__main__":
    download_dataset()
