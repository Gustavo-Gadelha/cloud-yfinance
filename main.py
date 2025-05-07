import logging

import yfinance as yf
from pandas import DataFrame

from config import LOG_FILE_PATH, CSV_DIR, CURRENT_TIMESTAMP, TICKERS_FILE

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)


def download_history(symbol: str, period: str, interval: str) -> DataFrame | None:
    ticker = yf.Ticker(symbol)

    try:
        return ticker.history(period, interval)
    except Exception as e:
        logging.error(f'Erro ao baixar histórico de {symbol}: {e}')
        return None


if __name__ == '__main__':
    logging.info('Iniciando coleta de dados do Yahoo Finance')

    with open(TICKERS_FILE) as file:
        tickers = file.read().splitlines()

    for symbol in tickers:
        logging.info(f'Processando {symbol}')
        history_data = download_history(symbol, '1d', '5m')
        if not history_data or history_data.empty:
            logging.warning(f'Nenhum dado histórico encontrado para {symbol}')
            continue

        file_path = CSV_DIR / symbol / f'history_{CURRENT_TIMESTAMP}.csv'
        file_path.parent.mkdir(parents=True, exist_ok=True)
        history_data.to_csv(file_path)
        logging.info(f'Dados de {symbol} salvos com sucesso em: {file_path}')

    logging.info('Coleta finalizada')
