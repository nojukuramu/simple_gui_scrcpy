@echo off
REM Silent launcher - no console window

REM Initialize conda for batch script
call conda activate aisa_env 2>nul

REM Launch the GUI with pythonw (no console window)
start "" pythonw "%~dp0scrcpy_gui.py"
