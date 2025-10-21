@echo off
setlocal

set "ORIGINAL_DIR=%cd%"
cd /d "%~dp0"

echo.
echo #RUNNING SCRIPT IN: %ORIGINAL_DIR%...
echo.

python -u auto.py "%ORIGINAL_DIR%"

endlocal
