@echo off
REM Navigate to project folder
cd C:\Users\PHYNO ZEUS\switch\data-engineering-roadmap-2025\week1

REM Activate virtual environment
call ..\venv\Scripts\activate.bat

REM Run script and save logs
python -Xutf8 week1_day4_auto_reports.py > run_log.txt 2>&1

