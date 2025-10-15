@echo off
title Scrcpy GUI Launcher

REM Initialize conda for batch script
echo Initializing conda environment...
call conda activate aisa_env

if errorlevel 1 (
    echo WARNING: Could not activate conda environment 'aisa_env'
    echo Trying with base Python...
    echo.
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    echo Or check your conda installation
    pause
    exit /b 1
)

REM Launch the GUI
echo Starting Scrcpy GUI...
python "%~dp0scrcpy_gui.py"

if errorlevel 1 (
    echo.
    echo ERROR: Failed to launch GUI
    pause
)
