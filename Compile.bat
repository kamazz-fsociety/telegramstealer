echo off

pip install --upgrade pip
pip install pyinstaller
pip install requests
pyinstaller -F -w -i test.ico codetg.py


rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null
