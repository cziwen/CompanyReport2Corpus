# config.py
"""
Configuration for SEC filings scraping pipeline.
Generates individual text files per filing.
"""

# SEC EDGAR search-filings endpoint
SEC_SEARCH_URL = 'https://www.sec.gov/search-filings'

USER_AGENT = 'companyreport2corpus/1.0 yours@mail.com'

COMPANIES = [
    # 'AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JNJ', 'V', 'UNH',
    # 'PG', 'MA', 'HD', 'LLY', 'BAC', 'XOM', 'PFE', 'KO', 'ABBV', 'MRK', 'DIS',
    # 'CSCO', 'PEP', 'AVGO', 'INTC', 'ABT', 'ADBE', 'CRM', 'TMO', 'NKE', 'CVX',
    # 'MCD', 'WMT', 'ORCL', 'CMCSA', 'NFLX', 'TXN', 'ACN', 'COST', 'AMGN', 'DHR',
    # 'HON', 'QCOM', 'SBUX', 'IBM', 'MDT', 'MDLZ', 'MMM', 'BA', 'CAT', 'GE', 'LMT',
    # 'UPS', 'UNP', 'RTX', 'GD', 'EMR', 'F', 'GM', 'MO', 'PM', 'DE', 'USB', 'PNC',
    # 'WFC', 'C', 'BLK', 'SPGI', 'ZTS', 'ADP', 'CVS', 'T', 'VZ', 'TMUS', 'AMD',
    # 'TSM', 'ASML', 'SAP', 'SONY', 'BABA', 'BIDU', 'TCEHY', 'NIO', 'LI', 'XPEV',
    # 'RIVN', 'COIN', 'PYPL', 'SQ', 'SHOP', 'UBER', 'LYFT', 'ZM', 'SPOT', 'DOCU',
    # 'PLTR', 'DDOG', 'MDB', 'NET', 'JPM', 'GS', 'CME', 'ICE', 'NDAQ', 'CSX', 'NSC',
    # 'MET', 'AXP', 'BK', 'FE', 'ED',
    # 'AEP', 'AIG', 'AJG', 'AKAM', 'ALB', 'ALL', 'ALXN', 'AMAT', 'AMP', 'ANET',
    # 'APH', 'ARE', 'ATO', 'AXON', 'AZO', 'BAX', 'BDX', 'BEN', 'BIIB', 'BKNG',
    # 'BR', 'BSX', 'BXP', 'CB', 'CDNS', 'CE', 'CHD', 'CI', 'CINF', 'CL', 'CLX',
    # 'CNC', 'COF', 'CPB', 'CTAS', 'CTSH', 'CTVA', 'DG', 'DLR', 'DLTR', 'DPZ',
    # 'DRI', 'EBAY', 'EL', 'ETN', 'EXC', 'EXPE', 'FAST', 'FIS', 'FISV', 'FLT',
    # 'FMC', 'FTNT', 'GDOT', 'GILD', 'GLW', 'GPC', 'GRMN', 'HAL', 'HAS', 'HCA',
    # 'HES', 'HIG', 'HLT', 'HPQ', 'HRL', 'HSY', 'IFF', 'ILMN', 'IP', 'IQV', 'IR',
    # 'IT', 'ITW', 'JBHT', 'JKHY', 'JNPR', 'K', 'KEY', 'KHC', 'KLAC', 'KMB', 'KR',
    # 'L', 'LDOS', 'LEG', 'LEN', 'LH', 'LIN', 'LKQ', 'LNC', 'LNT', 'LOW', 'LUV',
    # 'LW', 'MAS', 'MKC', 'MLM', 'MNST', 'MS'
]

COMPANIES += [
    'MMM', 'AOS', 'AES', 'AFL', 'A', 'ALLE', 'ATO', 'AMP', 'AWK', 'AJG', 'ALLE',
    'APH', 'APD', 'AVY', 'BKR', 'BLL', 'BK', 'BBY', 'BIIB', 'BLK', 'BAC', 'BAX',
    'BDX', 'BBWI', 'BR', 'BBY', 'BXP', 'CZR', 'CBRE', 'CF', 'CARR', 'CE', 'CNC',
    'CERN', 'CHTR', 'CI', 'CMS', 'COG', 'COST', 'CLX', 'CME', 'CMG', 'CB',
    'CNC', 'CNP', 'CTLT', 'COO', 'CPRT', 'CSRA', 'CINF', 'CTAS', 'CXO', 'DRC',
    'DD', 'DOV', 'DOW', 'DRE', 'DUK', 'DXC', 'EMN', 'ETR', 'EOG', 'ETFC',
    'EFX', 'EQIX', 'EQR', 'ESS', 'ELV', 'ES', 'EXR', 'FAST', 'FRT', 'FDX',
    'FIS', 'FITB', 'FE', 'FRC', 'FTV', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GRMN',
    'GIS', 'GWW', 'HAL', 'HAS', 'HOLX', 'HST', 'HSIC', 'HBAN', 'HIG', 'HWM',
    'HII', 'HLT', 'HP', 'HES', 'HSY', 'HPE', 'HUM', 'ITW', 'IDXX', 'ILMN', 'INTU',
    'ISRG', 'ICE', 'IFF', 'IPG', 'IRM', 'JBHT', 'JKHY', 'JCI', 'KHC', 'KMI',
    'KLAC', 'KMB', 'KIM', 'KMI', 'KR', 'LHX', 'LH', 'LRCX', 'LNC', 'LNT', 'LNW',
    'LUV', 'LYB', 'MTB', 'MMC', 'MLM', 'MCHP', 'MU', 'MSCI', 'MS', 'MHK',
    'MCO', 'MKTX', 'MLTX', 'MKC', 'MOS', 'MSI', 'NAV', 'NLOK', 'NOC', 'NCLH',
    'NUE', 'NVDA', 'NEM', 'NFLX', 'NKE', 'NI', 'NSC', 'NTRS', 'NOC', 'NVR',
    'ORLY', 'PNR', 'PAYX', 'PEG', 'PNW', 'PPG', 'PPL', 'PFG', 'PRU', 'PEG',
    'QLYS', 'RSG', 'RE', 'REG', 'RMD', 'ROK', 'ROL', 'ROP', 'RCL', 'SPG',
    'STZ', 'SIVB', 'SNA', 'SWK', 'SLB', 'SYK', 'SNA', 'SEDG', 'STX', 'STE',
    'SO', 'SPG', 'SWKS', 'TDG', 'TEL', 'TGT', 'TEL', 'TMO', 'TFX', 'TWTR',
    'TROW', 'TT', 'TRV', 'TSCO', 'TXT', 'UDR', 'ULTA', 'UAA', 'UA', 'USB', 'VTR',
    'VRSK', 'VRSN', 'VRTX', 'VZ', 'VMC', 'WBA', 'WMT', 'WELL', 'WBD', 'WM',
    'WAT', 'WEC', 'WFC', 'WELL', 'WRK', 'WY', 'XEL', 'XRX', 'XLNX', 'XYL', 'ZBH',
    'ZION', 'ZTS'
]

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
OUTPUT_DIR = 'output/corpus-10KQ'

# Filename template for each report
# Available placeholders: {company}, {year}, {form_type}, {accession}
FILENAME_TEMPLATE = '{company}_{year}_{form_type}_{accession}.txt'

# Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = 'INFO'
