@echo off
echo Starting Debug GUI Tool...
echo.

cd /d "%~dp0"

echo Opening debug interface in browser...
echo Please wait...
echo.

:: Clear cache and run
echo Clearing Streamlit cache...
echo.
streamlit cache clear
python -m streamlit run gui/streamlit_debug_gui.py --server.port 8502

pause
