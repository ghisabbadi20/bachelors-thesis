# This file only serves the purpose of containing the necessary Paths for loading/saving data

from pathlib import Path

PROJECT_ROOT = Path().resolve().parent
DATA_PATH = PROJECT_ROOT / "datos"
RESULTS_PATH = PROJECT_ROOT / "resultados"
