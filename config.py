# config.py
"""
Configuration for SEC filings scraping pipeline.
Generates individual text files per filing.
"""

# SEC EDGAR search-filings endpoint
SEC_SEARCH_URL = 'https://www.sec.gov/search-filings'

USER_AGENT = 'companyreport2corpus/1.0 yours@mail.com'

more_stocks = [
    'AEP', 'AIG', 'AJG', 'AKAM', 'ALB', 'ALL', 'ALXN', 'AMAT', 'AMP', 'ANET',
    'APH', 'ARE', 'ATO', 'AXON', 'AZO', 'BAX', 'BDX', 'BEN', 'BIIB', 'BKNG',
    'BR', 'BSX', 'BXP', 'CB', 'CDNS', 'CE', 'CHD', 'CI', 'CINF', 'CL', 'CLX',
    'CNC', 'COF', 'CPB', 'CTAS', 'CTSH', 'CTVA', 'DG', 'DLR', 'DLTR', 'DPZ',
    'DRI', 'EBAY', 'EL', 'ETN', 'EXC', 'EXPE', 'FAST', 'FIS', 'FISV', 'FLT',
    'FMC', 'FTNT', 'GDOT', 'GILD', 'GLW', 'GPC', 'GRMN', 'HAL', 'HAS', 'HCA',
    'HES', 'HIG', 'HLT', 'HPQ', 'HRL', 'HSY', 'ICE', 'IFF', 'ILMN', 'IP',
    'IQV', 'IR', 'IT', 'ITW', 'JBHT', 'JKHY', 'JNPR', 'K', 'KEY', 'KHC',
    'KLAC', 'KMB', 'KR', 'L', 'LDOS', 'LEG', 'LEN', 'LH', 'LIN', 'LKQ',
    'LNC', 'LNT', 'LOW', 'LUV', 'LW', 'MAS', 'MKC', 'MLM', 'MNST', 'MS'
]

COMPANIES = more_stocks

# List of company tickers or CIK identifiers to fetch
# COMPANIES = [
#     'AAPL',
#     'MSFT',
#     'NVDA',
#     'AMZN',
#     'GOOGL',
#     'META',
#     'TSLA',
#     'JNJ',
#     'V',
#     'UNH',
#     'PG',
#     'MA',
#     'HD',
#     'LLY',
#     'BAC',
#     'XOM',
#     'PFE',
#     'KO',
#     'ABBV',
#     'MRK',
#     'DIS',
#     'CSCO',
#     'PEP',
#     'AVGO',
#     'INTC',
#     'ABT',
#     'ADBE',
#     'CRM',
#     'TMO',
#     'NKE',
#     'CVX',
#     'MCD',
#     'WMT',
#     'ORCL',
#     'CMCSA',
#     'NFLX',
#     'TXN',
#     'ACN',
#     'COST',
#     'AMGN',
#     'DHR',
#     'HON',
#     'QCOM',
#     'SBUX',
#     'IBM',
#     'MDT',
#     'MDLZ',
#     'MMM',
#     'BA',
#     'CAT',
#     'GE',
#     'LMT',
#     'UPS',
#     'UNP',
#     'RTX',
#     'GD',
#     'EMR',
#     'F',
#     'GM',
#     'MO',
#     'PM',
#     'DE',
#     'USB',
#     'PNC',
#     'WFC',
#     'C',
#     'BLK',
#     'SPGI',
#     'ZTS',
#     'ADP',
#     'CVS',
#     'T',
#     'VZ',
#     'TMUS',
#     'AMD',
#     'TSM',
#     'ASML',
#     'SAP',
#     'SONY',
#     'BABA',
#     'BIDU',
#     'TCEHY',
#     'NIO',
#     'LI',
#     'XPEV',
#     'RIVN',
#     'COIN',
#     'PYPL',
#     'SQ',
#     'SHOP',
#     'UBER',
#     'LYFT',
#     'ZM',
#     'SPOT',
#     'DOCU',
#     'PLTR',
#     'DDOG',
#     'MDB',
#     'NET',
#     'JPM',
#     'GS',
#     'CME',
#     'ICE',
#     'NDAQ',
#     'CSX',
#     'NSC',
#     'MET',
#     'AXP',
#     'BK',
#     'FE',
#     'ED',
#     # Add more tickers or CIKs as needed
# ]

# List of years for which to scrape filings
YEARS = [
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022,
    2023,
    2024,
    2025,
]

# SEC form types to download (e.g., annual and quarterly reports)
FORM_TYPES = [
    # '10-K',
    # '10-Q',
    '8-k'
]

# Directory to output individual report files
OUTPUT_DIR = 'output/corpus-8k/'

# Filename template for each report
# Available placeholders: {company}, {year}, {form_type}, {accession}
FILENAME_TEMPLATE = '{company}_{year}_{form_type}_{accession}.txt'

# Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = 'INFO'
