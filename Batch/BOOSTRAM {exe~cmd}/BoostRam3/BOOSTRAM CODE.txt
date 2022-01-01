@echo off
title BOOSTRAM V.03 LAST EDITION
COLOR 9F

echo **************************************************************
echo BOOSTRAM V.03 LAST EDITION
echo                          BY Stefanos Stefanou
echo **************************************************************


echo Welcome to last edition of BOOSTRAM by Stefanos Stefanou
echo choose clean level
:again
echo 1 = minimum{fast}
echo 2 = maximum
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto minimum
If /i "%_dept%"=="2" goto maximum
If /i not "%_dept%"=="1" goto fail
If /i not "%_dept%"=="2" goto fail



:minimum
echo minumum level cleans only your ram
echo please press any key for clean your ram
pause >nul
start BOOSTRAM.VBE
echo BOOST complete pless any key for exit
pause >nul
exit

:maximum
echo full clean cleans all your system
echo start with disk cleanup
start cleanmgr.exe
echo press any key for continue...
pause >nul
echo next must defrag your pc
pause >nul
start dfrgui.exe
echo press any key for continue...
pause >nul
echo now must clean your ram
echo press any key for clean ram
pause >nul
start BOOSTRAM.VBE
echo clean complete press any key for exit
pause >nul
exit

:fail
echo Please enter one of the available commands
goto again
