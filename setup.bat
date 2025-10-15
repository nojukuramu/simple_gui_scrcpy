@echo off
title Scrcpy GUI - First Time Setup
echo.
echo ================================================
echo   Scrcpy GUI Wrapper - First Time Setup
echo ================================================
echo.
echo This script will help you set up the application.
echo.
pause

REM Check if env_config.json exists
if exist "config\env_config.json" (
    echo [OK] Configuration file already exists.
    echo.
    choice /C YN /M "Do you want to reconfigure"
    if errorlevel 2 goto :skip_config
)

echo.
echo Step 1: Python Environment Configuration
echo ========================================
echo.
echo What type of Python environment do you use?
echo.
echo 1. Conda (Anaconda/Miniconda)
echo 2. Virtual Environment (venv)
echo 3. System Python
echo 4. Skip (I'll configure manually)
echo.
choice /C 1234 /N /M "Select option (1-4): "

if errorlevel 4 goto :skip_config
if errorlevel 3 goto :system_python
if errorlevel 2 goto :venv_python
if errorlevel 1 goto :conda_python

:conda_python
echo.
echo Conda Environment Setup
echo ----------------------
echo.
set /p ENV_NAME="Enter your conda environment name (e.g., myenv): "
echo.
echo Creating configuration file...
(
    echo {
    echo     "environment": {
    echo         "type": "conda",
    echo         "name": "%ENV_NAME%",
    echo         "activate_command": "conda activate %ENV_NAME%"
    echo     },
    echo     "python": {
    echo         "executable": "python",
    echo         "use_pythonw": true
    echo     }
    echo }
) > "config\env_config.json"
echo [OK] Configuration created for conda environment: %ENV_NAME%
goto :test_setup

:venv_python
echo.
echo Virtual Environment Setup
echo -------------------------
echo.
set /p VENV_PATH="Enter full path to your venv folder: "
echo.
echo Creating configuration file...
(
    echo {
    echo     "environment": {
    echo         "type": "venv",
    echo         "name": "venv",
    echo         "activate_command": "%VENV_PATH%\\Scripts\\activate"
    echo     },
    echo     "python": {
    echo         "executable": "python",
    echo         "use_pythonw": true
    echo     }
    echo }
) > "config\env_config.json"
echo [OK] Configuration created for venv: %VENV_PATH%
goto :test_setup

:system_python
echo.
echo System Python Setup
echo -------------------
echo.
echo Creating configuration file...
(
    echo {
    echo     "environment": {
    echo         "type": "system",
    echo         "name": "system",
    echo         "activate_command": ""
    echo     },
    echo     "python": {
    echo         "executable": "python",
    echo         "use_pythonw": true
    echo     }
    echo }
) > "config\env_config.json"
echo [OK] Configuration created for system Python
goto :test_setup

:skip_config
echo.
echo [INFO] Skipping configuration.
echo Please edit config\env_config.json manually.
echo See docs\CONFIG_EXAMPLES.md for examples.
echo.

:test_setup
echo.
echo Step 2: Testing Setup
echo ====================
echo.
echo Running diagnostic test...
echo.
pause
call "tools\test_setup.bat"

echo.
echo.
echo ================================================
echo   Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Launch the GUI: launch_gui.bat or launch_gui.vbs
echo 2. Go to Settings tab
echo 3. Configure your scrcpy installation path
echo 4. Connect your device!
echo.
echo Documentation: See docs\ folder
echo Quick Reference: docs\QUICK_REFERENCE.txt
echo.
pause
