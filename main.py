# main.py
"""
Entry point for the SEC filings to individual TXT pipeline.
"""
import os
import sys
from downloader.sec_fetcher import SecFetcher
from parser.html_cleaner import HTMLCleaner
from utils.logger import get_logger
import config

def main():
    logger = get_logger(__name__, level=config.LOG_LEVEL)

    # Ensure output directory exists
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)

    # Initialize components
    fetcher = SecFetcher(sleep_time=0.1, user_agent=config.USER_AGENT)
    cleaner = HTMLCleaner()

    # Loop over parameters
    for company in config.COMPANIES:
        for year in config.YEARS:
            for form_type in config.FORM_TYPES:
                logger.info(f"Fetching {form_type} filings for {company} in {year}")
                filings = fetcher.fetch_filings(
                    company=company,
                    year=year,
                    form_type=form_type
                )
                for filing in filings:
                    accession = filing.get('accession', '').replace('/', '_')
                    # Build filename and path
                    safe_form = form_type.replace('/', '-')
                    filename = config.FILENAME_TEMPLATE.format(
                        company=company,
                        year=year,
                        form_type=safe_form,
                        accession=accession
                    )
                    filepath = os.path.join(config.OUTPUT_DIR, filename)
                    try:
                        html = fetcher.download_filing(filing)
                        text = cleaner.clean(html)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(text)
                        logger.info(f"Wrote cleaned text to {filepath}")
                    except Exception as e:
                        logger.error(f"Error processing {accession}: {e}")

    logger.info("Finished processing all filings.")

if __name__ == '__main__':
    main()
