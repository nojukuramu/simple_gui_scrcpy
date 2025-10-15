@echo off
title Scrcpy GUI Launcher
setlocal enabledelayedexpansion

REM Get the project root directory (parent of launchers folder)
set "PROJECT_ROOT=%~dp0.."
cd /d "%PROJECT_ROOT%"

REM Configuration file path
set "CONFIG_FILE=%PROJECT_ROOT%\config\env_config.json"

REM Default values
set "ENV_TYPE=conda"
set "ENV_NAME=aisa_env"
set "ACTIVATE_CMD=conda activate aisa_env"
set "USE_PYTHONW=true"

REM Check if config file exists
if exist "%CONFIG_FILE%" (
    echo Reading environment configuration...
    
    REM Parse JSON config file using PowerShell
    for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.type } catch { Write-Output 'conda' }"`) do set "ENV_TYPE=%%i"
    
    for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.name } catch { Write-Output 'aisa_env' }"`) do set "ENV_NAME=%%i"
    
    for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.activate_command } catch { Write-Output 'conda activate aisa_env' }"`) do set "ACTIVATE_CMD=%%i"
    
    for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.python.use_pythonw } catch { Write-Output 'true' }"`) do set "USE_PYTHONW=%%i"
    
    echo Environment Type: !ENV_TYPE!
    echo Environment Name: !ENV_NAME!
    echo.
) else (
    echo Warning: Configuration file not found. Using defaults.
    echo Creating default configuration file...
    
    REM Create default config file
    (
        echo {
        echo     "environment": {
        echo         "type": "conda",
        echo         "name": "aisa_env",
        echo         "activate_command": "conda activate aisa_env"
        echo     },
        echo     "python": {
        echo         "executable": "python",
        echo         "use_pythonw": true
        echo     }
        echo }
    ) > "%CONFIG_FILE%"
    echo.
)

REM Activate environment based on type
if /i "!ENV_TYPE!"=="conda" (
    echo Activating Conda environment: !ENV_NAME!...
    call !ACTIVATE_CMD!
    if errorlevel 1 (
        echo WARNING: Could not activate conda environment '!ENV_NAME!'
        echo Trying with base Python...
        echo.
    )
) else if /i "!ENV_TYPE!"=="venv" (
    echo Activating Virtual environment: !ENV_NAME!...
    call !ACTIVATE_CMD!
    if errorlevel 1 (
        echo WARNING: Could not activate virtual environment
        echo Trying with base Python...
        echo.
    )
) else if /i "!ENV_TYPE!"=="custom" (
    echo Running custom activation command...
    call !ACTIVATE_CMD!
    if errorlevel 1 (
        echo WARNING: Custom activation failed
        echo Trying with base Python...
        echo.
    )
) else if /i "!ENV_TYPE!"=="system" (
    echo Using system Python (no environment activation)
) else (
    echo Unknown environment type: !ENV_TYPE!
    echo Using system Python...
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please check:
    echo 1. Python is installed
    echo 2. Environment is activated correctly
    echo 3. Configuration in env_config.json is correct
    pause
    exit /b 1
)

echo Python found: 
python --version
echo.

REM Launch the GUI
echo Starting Scrcpy GUI...

if /i "!USE_PYTHONW!"=="true" (
    echo Using pythonw (no console window)...
    echo.
    echo Launching GUI in background...
    start "" pythonw "%PROJECT_ROOT%\src\scrcpy_gui.py"
    timeout /t 1 >nul
    echo.
    echo GUI should now be starting. If nothing appears:
    echo - Check if tkinter is installed
    echo - Run with use_pythonw=false in config\env_config.json to see errors
    echo.
    echo Press any key to close this window...
    pause >nul
) else (
    echo Using python (with console window)...
    python "%PROJECT_ROOT%\src\scrcpy_gui.py"
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to launch GUI
        echo.
        echo Troubleshooting:
        echo 1. Check if src\scrcpy_gui.py exists
        echo 2. Verify Python environment is correct
        echo 3. Check config\env_config.json configuration
        pause
        exit /b 1
    )
)

echo.
echo GUI launched successfully!
timeout /t 2 >nul
