echo off

pyinstaller -F -w -i test.ico auto.py


rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null