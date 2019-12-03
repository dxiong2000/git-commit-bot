@echo off
:loop
set /a num=%random% %%15 + 2
py script.py %num%
TIMEOUT /T 86400 /NOBREAK >nul
goto loop