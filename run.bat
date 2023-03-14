@echo off

(
    rem Change to the directory containing the script
    cd /d "%~dp0"

    echo Activate the virtual environment
    .\venv\Scripts\activate

    @echo on
    echo Running the script in Python...
    python main.py
    @echo off

    rem Deactivate the virtual environment
    deactivate

    timeout /t 1
)
