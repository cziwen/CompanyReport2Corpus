# downloader/sec_fetcher.py
"""
Module: sec_fetcher
Provides SecFetcher to lookup CIK, query SEC submissions API, and download filings.
"""
import requests
import time
from typing import List, Dict


class SecFetcher:
    # Endpoints for CIK mapping and submissions
    CIK_MAPPING_URL = 'https://www.sec.gov/files/company_tickers.json'
    SUBMISSIONS_URL = 'https://data.sec.gov/submissions/CIK{cik}.json'

    def __init__(self,
                 sleep_time: float = 0.5,
                 user_agent: str = 'companyreport2corpus/1.0 your_email@example.com'):
        """
        :param sleep_time: delay between requests to respect SEC rate limits
        :param user_agent: User-Agent header for SEC compliance (include contact info)
        """
        self.sleep_time = sleep_time
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': user_agent,
            'Accept': 'application/json'
        })
        # Load ticker-to-CIK map once
        self.cik_map = self._load_cik_map()

    def _load_cik_map(self) -> Dict[str, str]:
        """
        Download and parse the SEC ticker-to-CIK mapping.
        Returns a dict mapping lowercase ticker to 10-digit CIK string.
        """
        resp = self.session.get(self.CIK_MAPPING_URL)
        resp.raise_for_status()
        data = resp.json()  # dict: index -> {cik_str, ticker, title}

        mapping: Dict[str, str] = {}
        for entry in data.values():
            ticker = entry.get('ticker', '').lower()
            cik_str = str(entry.get('cik_str', '')).zfill(10)
            mapping[ticker] = cik_str
        time.sleep(self.sleep_time)
        return mapping

    def get_cik(self, ticker: str) -> str:
        """
        Return the 10-digit CIK corresponding to the given ticker.
        """
        cik = self.cik_map.get(ticker.lower())
        if not cik:
            raise ValueError(f'CIK not found for ticker: {ticker}')
        return cik

    def fetch_filings(self, company: str, year: int, form_type: str) -> List[Dict]:
        """
        Fetch metadata of filings for a given company ticker, year, and form type.
        Uses the SEC submissions JSON endpoint.

        Returns:
            List of dicts: {'accession', 'cik', 'primary_document'}
        """
        try:
            cik = self.get_cik(company)
        except ValueError:
            # Skip tickers without a CIK
            return []

        url = self.SUBMISSIONS_URL.format(cik=cik)
        resp = self.session.get(url)
        resp.raise_for_status()
        data = resp.json()

        filings: List[Dict] = []
        recent = data.get('filings', {}).get('recent', {})
        forms = recent.get('form', [])
        dates = recent.get('filingDate', [])
        accessions = recent.get('accessionNumber', [])
        primary_docs = recent.get('primaryDocument', [])

        for form, date, acc, doc in zip(forms, dates, accessions, primary_docs):
            if form.upper() == form_type.upper() and date.startswith(str(year)):
                filings.append({
                    'accession': acc,
                    'cik': cik,
                    'primary_document': doc
                })
        time.sleep(self.sleep_time)
        return filings

    def download_filing(self, filing: Dict) -> str:
        """
        Download the full text of a filing using the EDGAR Archives URL.

        Expects filing to contain 'cik', 'accession', and 'primary_document'.
        Returns raw HTML/text content.
        """
        # Remove leading zeros for directory path
        cik_int = str(int(filing['cik']))
        # Remove dashes for folder name
        accession_nodash = filing['accession'].replace('-', '')
        # Build URL: e.g., https://www.sec.gov/Archives/edgar/data/320193/000032019321000065/aapl-20211231.htm
        url = (
            f"https://www.sec.gov/Archives/edgar/data/"
            f"{cik_int}/{accession_nodash}/{filing['primary_document']}"
        )
        resp = self.session.get(url)
        resp.raise_for_status()
        time.sleep(self.sleep_time)
        return resp.text
