@echo off
set "VENVDIR=venv"
set "VENV_PATH=%CD%\bot\%VENVDIR%"
set "ACTIVATE_PATH=%VENV_PATH%\Scripts\activate.bat"
set "REQPATH=%CD%\requirements.txt"

if NOT EXIST "%ACTIVATE_PATH%" (
    echo Creating the virtual environment..
    py -3.12 -m venv "%VENV_PATH%"
) ELSE (
    echo Virtual environment already exists. Activating!
)

cd /d "%CD%\bot"
call "%ACTIVATE_PATH%"

if EXIST "%REQPATH%" (
    echo Installing requirements..
    pip install -r "%REQPATH%"
)

cmd /k
