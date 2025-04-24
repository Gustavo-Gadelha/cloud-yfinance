# Coletor de Dados Financeiros com yFinance

Este projeto é um script Python que utiliza a biblioteca [yfinance](https://pypi.org/project/yfinance/) para coletar
dados históricos de ações listadas no arquivo `tickers.txt`. Os dados são salvos em arquivos `.csv` organizados por
ticker, com logs detalhados armazenados em uma pasta dedicada.

## Funcionalidades

- Leitura de símbolos de ações a partir de um arquivo `tickers.txt`
- Download de dados históricos com período diário e intervalo de 5 minutos
- Armazenamento dos dados em arquivos CSV nomeados com timestamp
- Geração de logs com informações de execução e possíveis erros

## Estrutura de Diretórios

- `csv/` - Armazena os arquivos CSV organizados por ticker
- `logs/` - Contém os arquivos de log da execução
- `tickers.txt` - Lista de símbolos de ações a serem processados
