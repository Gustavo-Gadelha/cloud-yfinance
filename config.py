from datetime import datetime, timezone
from pathlib import Path

CURRENT_TIMESTAMP: str = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')

BASE_DIR: Path = Path().resolve()

CSV_DIR: Path = BASE_DIR / 'csv'
CSV_DIR.mkdir(exist_ok=True)

LOG_DIR: Path = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)

TICKERS_FILE: Path = BASE_DIR / 'tickers.txt'

LOG_FILE_PATH: Path = LOG_DIR / f'yfinance_log_{CURRENT_TIMESTAMP}.log'
