@echo off
setlocal
pushd %~dp0
call .venv\Scripts\activate
pytest -s -q
echo.
pause