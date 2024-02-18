@echo off

setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set LIB_DIR=%SCRIPT_DIR%lib
set PYTUBE_DIR=%LIB_DIR%\pytube

pip show pytube >nul 2>nul
if %errorlevel% neq 0 (
  
    echo Installing pytube...
    pip install pytube -t "%LIB_DIR%"
)


python -c "from pytube import __version__; print('pytube version:', __version__)"

set /p video_url=URL YouTube: 
set /p output_path=Directory (or ENTER): 
set /p resolution=Resolution (or ENTER): 

if not defined output_path set output_path=.

python download_youtube.py !video_url! !output_path! !resolution!

pause
endlocal
