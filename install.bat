@echo off

rem Create a new virtual environment
python -m venv venv

echo Activating the virtual environment
.\venv\Scripts\activate

echo Installing required packages...
@echo on
pip install -r requirements.txt
@echo off

rem Deactivate the virtual environment
deactivate

echo INSTALLATION COMPLETE!

timeout /t 5