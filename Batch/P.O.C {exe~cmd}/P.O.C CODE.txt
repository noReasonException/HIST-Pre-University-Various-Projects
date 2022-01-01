@echo off
title P.O.C  v.01
color CF

echo *****************************************************
echo   P.O.C v.01
echo             by Stefanos Stefanoy
echo *****************************************************
echo the PCoptionschange {P.O.C}  program helps you to change easily all settings
echo of all panels 
echo Here is all panels of Windows
:menu
echo 1 = Main control
echo 2 = System's default
echo 3 = Registry {only for advanced users}
echo 4 = Command prompt {cmd] {only for advanced users}
echo 5 = Mobility Center windows 
echo 6 = Backup options
echo 7 = Exit
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto 01
If /i "%_dept%"=="2" goto 02
If /i "%_dept%"=="3" goto 03
If /i "%_dept%"=="4" goto 04
If /i "%_dept%"=="5" goto 05
If /i "%_dept%"=="6" goto 06
If /i "%_dept%"=="7" goto 07
If /i not "%_dept%"=="1" goto fail
If /i not "%_dept%"=="2" goto fail
If /i not "%_dept%"=="3" goto fail
If /i not "%_dept%"=="4" goto fail
If /i not "%_dept%"=="5" goto fail
If /i not "%_dept%"=="6" goto fail
If /i not "%_dept%"=="7" goto fail

:01
echo Main control is the main panel control of windows
echo Press any key for start
pause >nul
start control
echo now what do you whant to do
echo 1 = go to main menu
echo press enter = exit programm
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto menu
echo thank you for trying P.O.C
echo Press any key for exit
pause >nul
exit

:02
echo System's default panel set the systems defalt programms
echo Press any key for start
pause >nul
start %SystemRoot%\system32\control.exe /name Microsoft.DefaultPrograms
echo now what do you whant to do
echo 1 = go to main menu
echo press enter = exit programm
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto menu
echo thank you for trying P.O.C
echo Press any key for exit
pause >nul
exit

:03
echo The registry is a database containing all the system settings
echo because is very complicated only advanced users use it
echo press any key for start
pause >nul
start regedit
echo now what do you whant to do
echo 1 = go to main menu
echo press enter = exit programm
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto menu
echo thank you for trying P.O.C
echo press any key for exit
pause >nul
exit

:04
echo Command prompt runs text-based commands
echo because is very complicated only advanced users use it
echo if do you want see a coplete list of all CMD commands press 1
echo for continue press enter
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" start http://pcsupport.about.com/od/commandlinereference/tp/command-prompt-commands-p1.htm
echo press any key for start
pause >nul
start CMD
echo now what do you whant to do
echo 1 = go to main menu
echo press enter = exit programm
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto menu
echo thank you for trying P.O.C
echo press any key for exit
pause >nul
exit

:05
echo Mobility Center windows is a panel for change brightness 
echo options of battery .etc
echo press any key for start
pause >nul
start mblctr
echo now what do you whant to do
echo 1 = go to main menu
echo press enter = exit programm
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto menu
echo thank you for trying P.O.C
echo press any key for exit
pause >nul
exit

:06
echo Backup options
echo press any key for start
pause >nul
start sdclt
echo now what do you whant to do
echo 1 = go to main menu
echo press enter = exit programm
Set /P _dept=Please enter choice:
If /i "%_dept%"=="1" goto menu
echo thank you for trying P.O.C
echo press any key for exit
pause >nul
exit

:07
echo thank you for trying P.O.C
echo press any key for exit
pause >nul
exit

:fail
echo please enter a from the available options
goto menu


