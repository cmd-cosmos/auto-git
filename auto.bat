@echo off
setlocal

set "ORIGINAL_DIR=%cd%"
cd /d "%~dp0"

echo.
echo #RUNNING SCRIPT IN: %ORIGINAL_DIR%...
timeout /t 3
echo.

python -u auto.py "%ORIGINAL_DIR%"

endlocal
