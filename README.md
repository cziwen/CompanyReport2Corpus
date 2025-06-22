# CompanyReport2Corpus
Fetching company financial reports from sites and turning them into corpus for LMs


companyReport2corpus/
├── README.md
├── requirements.txt
├── main.py                     # 主程序入口
├── config.py                   # 可配置抓取参数（年份、公司、文种等）
├── downloader/
│   ├── __init__.py
│   └── sec_fetcher.py          # 抓取并解析 SEC 文件
├── parser/
│   ├── __init__.py
│   └── html_cleaner.py         # 提取年报文本并清洗
├── output/
│   └── corpus.txt              # 最终语料输出
└── utils/
    └── logger.py               # 简单日志模块