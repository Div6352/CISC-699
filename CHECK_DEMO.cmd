@echo off
cd /d "%~dp0"
".venv\Scripts\python.exe" -u present_demo.py --check
pause
