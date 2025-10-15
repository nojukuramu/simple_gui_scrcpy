@echo off
REM Silent launcher - no console window
setlocal enabledelayedexpansion

REM Get the project root directory (parent of launchers folder)
set "PROJECT_ROOT=%~dp0.."
cd /d "%PROJECT_ROOT%"

REM Configuration file path
set "CONFIG_FILE=%PROJECT_ROOT%\config\env_config.json"

REM Default values
set "ACTIVATE_CMD=conda activate aisa_env"

REM Read config if exists
if exist "%CONFIG_FILE%" (
    for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "try { $config = Get-Content '%CONFIG_FILE%' | ConvertFrom-Json; Write-Output $config.environment.activate_command } catch { Write-Output 'conda activate aisa_env' }"`) do set "ACTIVATE_CMD=%%i"
)

REM Initialize environment silently
call !ACTIVATE_CMD! 2>nul

REM Launch the GUI with pythonw (no console window)
start "" pythonw "%PROJECT_ROOT%\src\scrcpy_gui.py"
