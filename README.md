# CompanyReport2Corpus

A modular pipeline for downloading, cleaning, and converting SEC company reports into structured corpus data. This tool is designed for preparing clean financial text data for large language model (LLM) training, fine-tuning, or downstream analysis.

---

## Quick Start

1. **Install requirements**:
   ```bash
   pip install -r requirements.txt 
    ```

2.	**Configure parameters in `config.py`**:
-   agent user email
-	ticker list
-	years or quarters
-	output file path


3.  **run pipeline**:
    ```bash
    python main.py
    ```
    
4.	**Output**:
-	Cleaned plain text corpus will be saved under the `output/` directory.

5. **count tokens**(optional):
    ```bash
    python token_counter.py
    ```
- Count the number of tokens in the output file path

6. **convert txt to jsonl**(optional):
    ```bash
    python convert_txt2jsonl.py -f folder1 folder2 -o output.jsonl
    ```
- Convert txt files into single jsonl for continue pre-train or whatever

---

## Module Descriptions

### `downloader/`
- **sec_fetcher.py**  
  Contains logic to fetch SEC filings by CIK, ticker, or form type using EDGAR search or direct URL scraping.

### `parser/`
- **html_cleaner.py**  
  Parses and sanitizes raw HTML files, removing formatting noise, tables, and irrelevant metadata to produce clean paragraph-level text.

### `utils/`
- **config.py**  
  Stores configuration values used across the project, such as EDGAR base URLs, output folders, and file naming conventions.

### Project Root
- **main.py**  
  The orchestrator script that runs the full pipeline: fetches raw reports → cleans HTML → saves structured corpus.
- **token_counter.py**  
  Token counting tool for estimating cost or batching API requests. Compatible with models like GPT, Claude, Qwen, etc.
- **output/ (not showing at first)**  
  Directory where cleaned corpus data and any intermediate files are saved.
- **README.md**

---