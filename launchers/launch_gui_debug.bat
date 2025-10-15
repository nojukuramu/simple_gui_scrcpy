@echo off
title Scrcpy GUI - DEBUG MODE
setlocal enabledelayedexpansion

echo ================================================
echo SCRCPY GUI - DEBUG MODE
echo ================================================
echo.
echo This launcher will:
echo - Show all error messages
echo - Keep console window open
echo - Display detailed diagnostic info
echo.
echo ================================================
echo.

REM Get the project root directory (parent of launchers folder)
set "PROJECT_ROOT=%~dp0.."
cd /d "%PROJECT_ROOT%"

REM Configuration file path
set "CONFIG_FILE=%PROJECT_ROOT%\config\env_config.json"

REM Check if config exists
if not exist "%CONFIG_FILE%" (
    echo [WARNING] config\env_config.json not found!
    echo Creating default configuration...
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
    echo Default config created.
    echo.
)
echo [1/6] Reading configuration...
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.type } catch { Write-Output 'conda' }"`) do set "ENV_TYPE=%%i"
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.name } catch { Write-Output 'aisa_env' }"`) do set "ENV_NAME=%%i"
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.activate_command } catch { Write-Output 'conda activate aisa_env' }"`) do set "ACTIVATE_CMD=%%i"

echo    Environment Type: !ENV_TYPE!
echo    Environment Name: !ENV_NAME!
echo    Activate Command: !ACTIVATE_CMD!
echo.

echo [2/6] Activating Python environment...
if /i "!ENV_TYPE!"=="conda" (
    echo    Executing: !ACTIVATE_CMD!
    call !ACTIVATE_CMD!
    if errorlevel 1 (
        echo    [WARNING] Conda activation may have failed
        echo    This is OK if conda is not fully initialized
    ) else (
        echo    [OK] Conda environment activated
    )
) else if /i "!ENV_TYPE!"=="venv" (
    echo    Executing: !ACTIVATE_CMD!
    call !ACTIVATE_CMD!
) else if /i "!ENV_TYPE!"=="system" (
    echo    Using system Python (no activation)
) else if /i "!ENV_TYPE!"=="custom" (
    echo    Executing: !ACTIVATE_CMD!
    call !ACTIVATE_CMD!
)
echo.

echo [3/6] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo    [ERROR] Python NOT found!
    echo.
    echo    Possible solutions:
    echo    1. Install Python
    echo    2. Activate your conda/venv environment manually first
    echo    3. Check env_config.json settings
    echo.
    pause
    exit /b 1
) else (
    echo    [OK] Python found:
    python --version
    echo    Location:
    python -c "import sys; print('   ', sys.executable)"
)
echo.

echo [4/6] Checking tkinter...
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo    [ERROR] tkinter NOT found!
    echo.
    echo    To fix:
    echo    - For conda: conda install tk
    echo    - For pip: usually comes with Python
    echo.
    pause
    exit /b 1
) else (
    echo    [OK] tkinter is available
)
echo.

echo [5/6] Checking scrcpy_gui.py...
if not exist "%PROJECT_ROOT%\src\scrcpy_gui.py" (
    echo    [ERROR] src\scrcpy_gui.py not found!
    pause
    exit /b 1
) else (
    echo    [OK] scrcpy_gui.py found
)
echo.

echo [6/6] Launching GUI with full error display...
echo ================================================
echo.

REM Always use python (not pythonw) in debug mode to see errors
python "%PROJECT_ROOT%\src\scrcpy_gui.py"

echo.
echo ================================================
echo GUI has closed.
echo.
echo If the GUI didn't appear or crashed:
echo 1. Check the error messages above
echo 2. Make sure tkinter is installed
echo 3. Verify env_config.json is correct
echo 4. Check if scrcpy path is set correctly
echo.
echo Press any key to exit...
pause >nul
