@echo off
:: Check if the virtual environment is already activated
if not defined VIRTUAL_ENV (
    call venv\Scripts\activate
)
start cmd /k "python main.py"
timeout /t 5
start http://127.0.0.1:5000