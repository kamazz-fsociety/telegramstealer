echo off

pyinstaller -F -w -i test.ico codetg.py


rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null
