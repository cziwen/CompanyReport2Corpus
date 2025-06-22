# parser/html_cleaner.py
"""
Module: html_cleaner
Provides HTMLCleaner to strip HTML tags, remove Inline XBRL, and extract clean text from filings.
"""
from bs4 import BeautifulSoup
import re

class HTMLCleaner:
    def __init__(self):
        pass

    def clean(self, html: str) -> str:
        """
        Clean raw HTML content and extract plain text suitable for LLM training.

        Steps:
        1. Parse HTML with BeautifulSoup.
        2. Remove Inline XBRL tags (e.g., ix:*, xbrli:*).
        3. Remove <script>, <style>, <footer>, <nav>, <table>, <header>, <form> elements.
        4. Extract visible text.
        5. Remove URIs and XBRL-specific attributes.
        6. Collapse whitespace and normalize.
        """
        # Parse HTML
        soup = BeautifulSoup(html, 'html.parser')

        # 1. Remove Inline XBRL and namespaced tags (ix:*, xbrli:*, etc.)
        for tag in soup.find_all(lambda t: ':' in t.name):
            tag.decompose()

        # 2. Remove unwanted structural and noise elements
        for tag in soup(['script', 'style', 'footer', 'nav', 'table', 'header', 'form']):
            tag.decompose()

        # 3. Extract text
        text = soup.get_text(separator=' ')

        # 4. Remove any remaining URLs
        text = re.sub(r'https?://\S+', ' ', text)

        # 5. Remove XBRL attribute remnants like contextRef, unitRef, etc.
        text = re.sub(r'\b(contextRef|unitRef|decimals)="[^"]+"', ' ', text)

        # 6. Collapse multiple whitespace into single spaces
        text = re.sub(r'\s+', ' ', text)

        # Strip leading/trailing spaces
        return text.strip()
