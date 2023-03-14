@echo off

rem Create a new virtual environment
python -m venv venv

rem Activate the virtual environment
call .\venv\bin\activate.ps1

rem Install required packages
pip install -r requirements.txt

rem Deactivate the virtual environment
deactivate
