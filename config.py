import platform
from datetime import datetime
from pathlib import Path

IS_LINUX = 'linux' in platform.platform().lower()

CURRENT_TIMESTAMP: str = datetime.now().strftime('%Y%m%d_%H%M')

BASE_DIR: Path = Path(__file__).resolve().parent

if IS_LINUX:
    APACHE_DOCUMENT_ROOT: Path = Path('/var/www/html').resolve()
else:
    APACHE_DOCUMENT_ROOT: Path = BASE_DIR / 'var' / 'www' / 'html'
    APACHE_DOCUMENT_ROOT.mkdir(exist_ok=True, parents=True)

LOG_DIR: Path = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)

CSV_DIR: Path = APACHE_DOCUMENT_ROOT / 'csv'
CSV_DIR.mkdir(exist_ok=True)

TICKERS_FILE: Path = BASE_DIR / 'tickers.txt'

LOG_FILE_PATH: Path = LOG_DIR / f'yfinance_log_{CURRENT_TIMESTAMP}.log'
