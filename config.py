from datetime import datetime
from pathlib import Path

CURRENT_TIMESTAMP: str = datetime.now().strftime('%Y%m%d_%H%M')

BASE_DIR: Path = Path(__file__).resolve().parent

CSV_DIR: Path = BASE_DIR / 'csv'
CSV_DIR.mkdir(exist_ok=True)

LOG_DIR: Path = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)

TICKERS_FILE: Path = BASE_DIR / 'tickers.txt'

LOG_FILE_PATH: Path = LOG_DIR / f'yfinance_log_{CURRENT_TIMESTAMP}.log'
