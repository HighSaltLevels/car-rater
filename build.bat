@ECHO off

python -m pip install -r requirements.txt -r requirements-dev.txt

set PYTHONPATH="%PYTHONPATH%:%CD%\carrater"
pyinstaller -w -p "%CD%\carrater" -F -n "Car Rater" -i icon.ico carrater\__main__.py

PAUSE
