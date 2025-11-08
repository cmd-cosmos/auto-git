@echo off
setlocal

set "ORIGINAL_DIR=%cd%"
cd /d "%~dp0"

echo.
echo ======================== AUTO GIT ROUTINE ========================
echo.
echo # RUNNING SCRIPT IN: %ORIGINAL_DIR%...
timeout /t 2 /nobreak > NUL
echo.

python -u auto.py "%ORIGINAL_DIR%"

endlocal
