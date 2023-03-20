@echo off

REM Create the virtual environment
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Deactivate the virtual environment
deactivate

echo Dependencies installed successfully! Press enter to continue
pause