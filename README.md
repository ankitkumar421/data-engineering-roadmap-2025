# Data Engineering Roadmap 2025 🚀

This repo documents my step-by-step journey to become a Data Engineer, starting with **Week 1: ETL Pipelines with Python, SQLite, and Automation**.

---

## 📅 Week 1 Deliverables

### Day 1 — Pandas Basics
- Explored data cleaning, transformations, and revenue calculations using pandas.
- Notebook: [`week1_day1_pandas_basics.ipynb`](week1/week1_day1_pandas_basics.ipynb)

### Day 2 — Build ETL Pipeline
- Extracted raw CSV, transformed data (cleaning, typecasting), loaded into SQLite.
- Script: [`week1_day2_etl_pipeline.py`](week1/week1_day2_etl_pipeline.py)

### Day 3 — SQL Queries
- Queried SQLite with SQL for:
  - Total Revenue
  - Top Customers
  - Monthly Revenue
- Notebook: [`week1_day3_sql_queries.ipynb`](week1/week1_day3_sql_queries.ipynb)

### Day 4 — Automated Reports
- Python script to run SQL queries and save results to CSV & Excel.
- Script: [`week1_day4_auto_reports.py`](week1/week1_day4_auto_reports.py)
- Reports saved in [`week1/reports/`](week1/reports/)

### Day 5 — Scheduling
- Added batch file + Task Scheduler job to run pipeline daily.
- File: [`run_reports.bat`](run_reports.bat)

---

## 🛠️ Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/<your-username>/data-engineering-roadmap-2025.git
   cd data-engineering-roadmap-2025
