@echo off

rem Change to the directory containing the script
cd /d "%~dp0"

rem Activate the virtual environment
call .\venv\bin\activate.ps1

rem Run the Python script
python split.py

rem Deactivate the virtual environment
deactivate
