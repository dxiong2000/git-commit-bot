@echo off
set /a num=%random% %%15 + 2
py script.py %num%