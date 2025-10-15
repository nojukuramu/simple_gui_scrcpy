@echo off
title Scrcpy GUI - Diagnostic Test
setlocal enabledelayedexpansion

echo ================================================
echo SCRCPY GUI DIAGNOSTIC TEST
echo ================================================
echo.

REM Get the project root directory (parent of tools folder)
set "PROJECT_ROOT=%~dp0.."
cd /d "%PROJECT_ROOT%"

REM Test 1: Check if env_config.json exists
echo [Test 1] Checking for config\env_config.json...
set "CONFIG_FILE=%PROJECT_ROOT%\config\env_config.json"
if exist "%CONFIG_FILE%" (
    echo [PASS] Config file found at: %CONFIG_FILE%
) else (
    echo [FAIL] Config file NOT found!
    goto :end
)
echo.

REM Test 2: Parse config file
echo [Test 2] Parsing configuration...
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.type } catch { Write-Output 'ERROR' }"`) do set "ENV_TYPE=%%i"
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.name } catch { Write-Output 'ERROR' }"`) do set "ENV_NAME=%%i"
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.activate_command } catch { Write-Output 'ERROR' }"`) do set "ACTIVATE_CMD=%%i"
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.python.use_pythonw } catch { Write-Output 'ERROR' }"`) do set "USE_PYTHONW=%%i"

echo Environment Type: !ENV_TYPE!
echo Environment Name: !ENV_NAME!
echo Activate Command: !ACTIVATE_CMD!
echo Use pythonw: !USE_PYTHONW!

if "!ENV_TYPE!"=="ERROR" (
    echo [FAIL] Could not parse config file!
    goto :end
)
echo [PASS] Configuration parsed successfully
echo.

REM Test 3: Activate environment
echo [Test 3] Activating environment...
if /i "!ENV_TYPE!"=="conda" (
    echo Trying: !ACTIVATE_CMD!
    call !ACTIVATE_CMD!
    if errorlevel 1 (
        echo [WARN] Could not activate conda environment
        echo This may be OK if conda is not initialized in batch
    ) else (
        echo [PASS] Conda environment activated
    )
) else if /i "!ENV_TYPE!"=="system" (
    echo [INFO] Using system Python (no activation needed)
)
echo.

REM Test 4: Check Python
echo [Test 4] Checking Python availability...
python --version >nul 2>&1
if errorlevel 1 (
    echo [FAIL] Python NOT found in PATH!
    echo.
    echo Please check:
    echo - Python is installed
    echo - Conda environment is activated
    echo - Python is in your PATH
    goto :end
) else (
    echo [PASS] Python found:
    python --version
)
echo.

REM Test 5: Check Python executable path
echo [Test 5] Python executable location...
python -c "import sys; print('[INFO] Python executable:', sys.executable)"
echo.

REM Test 6: Check tkinter
echo [Test 6] Checking tkinter (required for GUI)...
python -c "import tkinter; print('[PASS] tkinter is available')" 2>nul
if errorlevel 1 (
    echo [FAIL] tkinter NOT available!
    echo.
    echo To fix:
    echo - For conda: conda install tk
    echo - For pip: pip install tk
    goto :end
)
echo.

REM Test 7: Check if scrcpy_gui.py exists
echo [Test 7] Checking for src\scrcpy_gui.py...
if exist "%PROJECT_ROOT%\src\scrcpy_gui.py" (
    echo [PASS] scrcpy_gui.py found
) else (
    echo [FAIL] scrcpy_gui.py NOT found!
    goto :end
)
echo.

REM Test 8: Check pythonw
echo [Test 8] Checking pythonw availability...
pythonw --version >nul 2>&1
if errorlevel 1 (
    echo [WARN] pythonw NOT found - will use python instead
    echo This means console window will show when launching
) else (
    echo [PASS] pythonw is available
    pythonw --version
)
echo.

echo ================================================
echo ALL TESTS COMPLETED
echo ================================================
echo.
echo If all tests passed, try launching the GUI with:
echo   Option 1: python "%PROJECT_ROOT%\src\scrcpy_gui.py"
echo   Option 2: pythonw "%PROJECT_ROOT%\src\scrcpy_gui.py"
echo.
echo Press any key to attempt GUI launch with python (console visible)...
pause >nul

echo.
echo Launching GUI with python (console visible for errors)...
python "%PROJECT_ROOT%\src\scrcpy_gui.py"

if errorlevel 1 (
    echo.
    echo [ERROR] GUI failed to launch!
    echo Check the error messages above.
)

:end
echo.
echo Press any key to exit...
pause >nul
