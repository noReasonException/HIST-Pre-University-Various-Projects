@echo off
color 0E
title CMDG-R v.2.0
echo +------------------------------------------------------------------------------+
echo 			BatchHelp Version 1.0 
echo 			By El_Sonador
echo +------------------------------------------------------------------------------+
:Restart
Set /P _dept=Ready= ~
If /i "%_dept%"=="Append" goto Append
If /i "%_dept%"=="Arp" goto Arp
If /i "%_dept%"=="Assoc" goto Assoc
If /i "%_dept%"=="At" goto At
If /i "%_dept%"=="Atmadm" goto Atmadm
If /i "%_dept%"=="Attrib" goto Attrib
If /i "%_dept%"=="Bootcfg" goto Bootcfg
If /i "%_dept%"=="Break" goto Break
If /i "%_dept%"=="Cacls" goto Cacls
If /i "%_dept%"=="Call" goto Call
If /i "%_dept%"=="Cd" goto Cd
If /i "%_dept%"=="Chdir" goto Chdir
If /i "%_dept%"=="Chkdsk" goto Chkdsk
If /i "%_dept%"=="Chkntfs" goto Chkntfs
If /i "%_dept%"=="Cipher" goto Cipher
If /i "%_dept%"=="Cls" goto Cls
If /i "%_dept%"=="Cmd" goto Cmd
If /i "%_dept%"=="Cmstp" goto Cmstp
If /i "%_dept%"=="Color" goto Color
If /i "%_dept%"=="Command" goto Command
If /i "%_dept%"=="Comp" goto Comp
If /i "%_dept%"=="Compact" goto Compact
If /i "%_dept%"=="Convert" goto Convert
If /i "%_dept%"=="Copy" goto Copy
If /i "%_dept%"=="Cscript" goto Cscript
If /i "%_dept%"=="Date" goto Date
If /i "%_dept%"=="Debug" goto Debug
If /i "%_dept%"=="Defrag" goto Defrag
If /i "%_dept%"=="Del" goto Del
If /i "%_dept%"=="Diantz" goto Diantz
If /i "%_dept%"=="Dir" goto Dir
If /i "%_dept%"=="Diskcomp" goto Diskcomp
If /i "%_dept%"=="Diskcopy" goto Diskcopy
If /i "%_dept%"=="Diskpart" goto Diskpart
If /i "%_dept%"=="Diskperf" goto Diskperf
If /i "%_dept%"=="Doskey" goto Doskey
If /i "%_dept%"=="Dosx" goto Dosx
If /i "%_dept%"=="Driverquery" goto Driverquery
If /i "%_dept%"=="Echo" goto Echo
If /i "%_dept%"=="Edit" goto Edit
If /i "%_dept%"=="Edlin" goto Edlin
If /i "%_dept%"=="Endlocal" goto Endlocal
If /i "%_dept%"=="Erase" goto Erase
If /i "%_dept%"=="Esentutl" goto Esentutl
If /i "%_dept%"=="Eventcreate" goto Eventcreate
If /i "%_dept%"=="Eventtriggers" goto Eventtriggers
If /i "%_dept%"=="Exe2bin" goto Exe2bin
If /i "%_dept%"=="Exit" goto Exit
If /i "%_dept%"=="Expand" goto Expand
If /i "%_dept%"=="Extrac32" goto Extrac32
If /i "%_dept%"=="fastopen" goto fastopen
If /i "%_dept%"=="Fc" goto Fc
If /i "%_dept%"=="Find" goto Find
If /i "%_dept%"=="Findstr" goto Findstr
If /i "%_dept%"=="Finger" goto Finger
If /i "%_dept%"=="Fltmc" goto Fltmc
If /i "%_dept%"=="For" goto For
If /i "%_dept%"=="Forcedos" goto Forcedos
If /i "%_dept%"=="Format" goto Format
If /i "%_dept%"=="Fsutil" goto Fsutil
If /i "%_dept%"=="Ftp" goto Ftp
If /i "%_dept%"=="Ftype" goto Ftype
If /i "%_dept%"=="Getmac" goto Getmac
If /i "%_dept%"=="Goto" goto Goto
If /i "%_dept%"=="Gpresult" goto Gpresult
If /i "%_dept%"=="Gpupdate" goto Gpupdate
If /i "%_dept%"=="Graftabl" goto Graftabl
If /i "%_dept%"=="Graphics" goto Graphics
If /i "%_dept%"=="Help" goto Help
If /i "%_dept%"=="Hostname" goto Hostname
If /i "%_dept%"=="If" goto If
If /i "%_dept%"=="Ipconfig" goto Ipconfig
If /i "%_dept%"=="Ipxroute" goto Ipxroute
If /i "%_dept%"=="Kb16" goto Kb16
If /i "%_dept%"=="Label" goto Label
If /i "%_dept%"=="Loadfix" goto Loadfix
If /i "%_dept%"=="Lodctr" goto Lodctr
If /i "%_dept%"=="Logman" goto Logman
If /i "%_dept%"=="Logoff" goto Logoff
If /i "%_dept%"=="Lpq" goto Lpq
If /i "%_dept%"=="Lpr" goto Lpr
If /i "%_dept%"=="Makecab" goto Makecab
If /i "%_dept%"=="Md" goto Md
If /i "%_dept%"=="Mem" goto Mem
If /i "%_dept%"=="Mkdir" goto Mkdir
If /i "%_dept%"=="Mode" goto Mode
If /i "%_dept%"=="More" goto More
If /i "%_dept%"=="Mountvol" goto Mountvol
If /i "%_dept%"=="Move" goto Move
If /i "%_dept%"=="Mrinfo" goto Mrinfo
If /i "%_dept%"=="Msg" goto Msg
If /i "%_dept%"=="Msiexec" goto Msiexec
If /i "%_dept%"=="Nbtstat" goto Nbtstat
If /i "%_dept%"=="Net" goto Net
If /i "%_dept%"=="Net1" goto Net1
If /i "%_dept%"=="Netsh" goto Netsh
If /i "%_dept%"=="Netstat" goto Netstat
If /i "%_dept%"=="Nlsfunc" goto Nlsfunc
If /i "%_dept%"=="Nslookup" goto Nslookup
If /i "%_dept%"=="Ntbackup" goto Ntbackup
If /i "%_dept%"=="Ntsd" goto Ntsd
If /i "%_dept%"=="Openfiles" goto Openfiles
If /i "%_dept%"=="Path" goto Path
If /i "%_dept%"=="Pathping" goto Pathping
If /i "%_dept%"=="Pause" goto Pause
If /i "%_dept%"=="Pentnt" goto Pentnt
If /i "%_dept%"=="Ping" goto Ping
If /i "%_dept%"=="Popd" goto Popd
If /i "%_dept%"=="Powercfg" goto Powercfg
If /i "%_dept%"=="Print" goto Print
If /i "%_dept%"=="Prompt" goto Prompt
If /i "%_dept%"=="Pushd" goto Pushd
If /i "%_dept%"=="Qappsrv" goto Qappsrv
If /i "%_dept%"=="Qprocess" goto Qprocess
If /i "%_dept%"=="Qwinsta" goto Qwinsta
If /i "%_dept%"=="Rasautou" goto Rasautou
If /i "%_dept%"=="Rasdial" goto Rasdial
If /i "%_dept%"=="Rcp" goto Rcp
If /i "%_dept%"=="Rd" goto Rd
If /i "%_dept%"=="Recover" goto Recover
If /i "%_dept%"=="Reg" goto Reg
If /i "%_dept%"=="Regini" goto Regini
If /i "%_dept%"=="Regsvr32" goto Regsvr32
If /i "%_dept%"=="Relog" goto Relog
If /i "%_dept%"=="Rem" goto Rem
If /i "%_dept%"=="Ren" goto Ren
If /i "%_dept%"=="Rename" goto Rename
If /i "%_dept%"=="Replace" goto Replace
If /i "%_dept%"=="Reset" goto Reset
If /i "%_dept%"=="Rexec" goto Rexec
If /i "%_dept%"=="Rmdir" goto Rmdir
If /i "%_dept%"=="Route" goto Route
If /i "%_dept%"=="Rsh" goto Rsh
If /i "%_dept%"=="Rsm" goto Rsm
If /i "%_dept%"=="Runas" goto Runas
If /i "%_dept%"=="Rwinsta" goto Rwinsta
If /i "%_dept%"=="Sc" goto Sc
If /i "%_dept%"=="Schtasks" goto Schtasks
If /i "%_dept%"=="Sdbinst" goto Sdbinst
If /i "%_dept%"=="Secedit" goto Secedit
If /i "%_dept%"=="Set" goto Set
If /i "%_dept%"=="Setlocal" goto Setlocal
If /i "%_dept%"=="Setver" goto Setver
If /i "%_dept%"=="Sfc" goto Sfc
If /i "%_dept%"=="Shadow" goto Shadow
If /i "%_dept%"=="Share" goto Share
If /i "%_dept%"=="Shift" goto Shift
If /i "%_dept%"=="Shutdown" goto Shutdown
If /i "%_dept%"=="Sort" goto Sort
If /i "%_dept%"=="Start" goto Start
If /i "%_dept%"=="Subst" goto Subst
If /i "%_dept%"=="Systeminfo" goto Systeminfo
If /i "%_dept%"=="Taskkill" goto Taskkill
If /i "%_dept%"=="Tasklist" goto Tasklist
If /i "%_dept%"=="Tcmsetup" goto Tcmsetup
If /i "%_dept%"=="Telnet" goto Telnet
If /i "%_dept%"=="Tftp" goto Tftp
If /i "%_dept%"=="Time" goto Time
If /i "%_dept%"=="Title" goto Title
If /i "%_dept%"=="Tlntadmn" goto Tlntadmn
If /i "%_dept%"=="Tracerpt" goto Tracerpt
If /i "%_dept%"=="Tracert" goto Tracert
If /i "%_dept%"=="Tree" goto Tree
If /i "%_dept%"=="Tscon" goto Tscon
If /i "%_dept%"=="Tsdiscon" goto Tsdiscon
If /i "%_dept%"=="Tskill" goto Tskill
If /i "%_dept%"=="Tsshutdn" goto Tsshutdn
If /i "%_dept%"=="Type" goto Type
If /i "%_dept%"=="Typeperf" goto Typeperf
If /i "%_dept%"=="Unlodctr" goto Unlodctr
If /i "%_dept%"=="Ver" goto Ver
If /i "%_dept%"=="Verify" goto Verify
If /i "%_dept%"=="Vol" goto Vol
If /i "%_dept%"=="Vssadmin" goto Vssadmin
If /i "%_dept%"=="W32tm" goto W32tm
If /i "%_dept%"=="Wmic" goto Wmic
If /i "%_dept%"=="Xcopy" goto Xcopy
If /i "%_dept%"=="Attrib" goto Attrib 
If /i "%_dept%"=="Auditpol" goto Auditpol 
If /i "%_dept%"=="Bcdedit" goto Bcdedit
If /i "%_dept%"=="Bitsadmin" goto Bitsadmin 
If /i "%_dept%"=="Certreq" goto Certreq 
If /i "%_dept%"=="Certutil" goto Certutil 
If /i "%_dept%"=="Change" goto Change 
If /i "%_dept%"=="Chcp" goto Chcp 
If /i "%_dept%"=="Chglogon" goto Chglogon
If /i "%_dept%"=="Chgport" goto Chgport
If /i "%_dept%"=="Chgusr" goto Chgusr
If /i "%_dept%"=="Choice" goto Choice 
If /i "%_dept%"=="Clip" goto Clip
If /i "%_dept%"=="Cmdkey" goto Cmdkey
If /i "%_dept%"=="Diskraid" goto Diskraid
If /i "%_dept%"=="Dispdiag" goto Dispdiag
If /i "%_dept%"=="Icacls" goto Icacls
If /i "%_dept%"=="Irftp" goto Irftp
If /i "%_dept%"=="Iscsicli" goto Iscsicli
If /i "%_dept%"=="Ktmutil" goto Ktmutil
If /i "%_dept%"=="Mklink" goto Mklink
If /i "%_dept%"=="Mount" goto Mount
If /i "%_dept%"=="Muiunattend" goto Muiunattend
If /i "%_dept%"=="Netcfg" goto Netcfg
If /i "%_dept%"=="Nfsadmin" goto Nfsadmin
If /i "%_dept%"=="Ocsetup" goto Ocsetup
If /i "%_dept%"=="Pkgmgr" goto Pkgmgr
If /i "%_dept%"=="Pnpunattend" goto Pnpunattend
If /i "%_dept%"=="Pnputil" goto Pnputil
If /i "%_dept%"=="Query" goto Query
If /i "%_dept%"=="Quser" goto Quser
If /i "%_dept%"=="Robocopy" goto Robocopy
If /i "%_dept%"=="Rpcinfo" goto Rpcinfo
If /i "%_dept%"=="Rpcping" goto Rpcping
If /i "%_dept%"=="Setx" goto Setx
If /i "%_dept%"=="Showmount" goto Showmount
If /i "%_dept%"=="Sxstrace" goto Sxstrace
If /i "%_dept%"=="Takeown" goto Takeown
If /i "%_dept%"=="Telnet" goto Telnet
If /i "%_dept%"=="Timeout" goto Timeout
If /i "%_dept%"=="Umount" goto Umount
If /i "%_dept%"=="Waitfor" goto Waitfor
If /i "%_dept%"=="Wbadmin" goto Wbadmin
If /i "%_dept%"=="Wecutil" goto Wecutil
If /i "%_dept%"=="Wevtutil" goto Wevtutil
If /i "%_dept%"=="Where" goto Where
If /i "%_dept%"=="Whoami" goto Whoami
If /i "%_dept%"=="Winrm" goto Winrm
If /i "%_dept%"=="Winrs" goto Winrs
If /i "%_dept%"=="Winsat" goto Winsat
If /i "%_dept%"=="Wsmanhttpconfig" goto Wsmanhttpconfig
If /i "%_dept%"=="Bcdboot" goto Bcdboot
If /i "%_dept%"=="Bdehdcfg" goto Bdehdcfg
If /i "%_dept%"=="Dism" goto Dism
If /i "%_dept%"=="Forfiles" goto Forfiles
If /i "%_dept%"=="Hwrcomp" goto Hwrcomp
If /i "%_dept%"=="Hwrreg" goto Hwrreg
If /i "%_dept%"=="Klist" goto Klist
If /i "%_dept%"=="Ksetup" goto Ksetup
If /i "%_dept%"=="Manage-bde" goto Manage-bde
If /i "%_dept%"=="Nltest" goto Nltest
If /i "%_dept%"=="Rdpsign" goto Rdpsign
If /i "%_dept%"=="Reagentc" goto Reagentc
If /i "%_dept%"=="Repair-bde" goto Repair-bde
If /i "%_dept%"=="Setspn" goto Setspn
If /i "%_dept%"=="Typerperf" goto Typerperf
If /i "%_dept%"=="Tzutil" goto Tzutil
If /i "%_dept%"=="Vaultcmd" goto Vaultcmd
If /i "%_dept%"=="Bootsect" goto Bootsect
If /i "%_dept%"=="Checknetisolation" goto Checknetisolation
If /i "%_dept%"=="Djoin" goto Djoin
If /i "%_dept%"=="Fondue" goto Fondue
If /i "%_dept%"=="Licensingdiag" goto Licensingdiag
If /i "%_dept%"=="Pwlauncher" goto Pwlauncher
If /i "%_dept%"=="Register-cimprovider" goto Register-cimprovider
If /i "%_dept%"=="Tpmvscmgr" goto Tpmvscmgr
If /i "%_dept%"=="Xwizard" goto Xwizard
goto Fail
:Fail
echo command not regognized
goto Restart

:Append
echo The append command can be used by programs to open files in another directory as if they were located in the current directory.
echo The append command is not available in 64-bit versions of Windows XP.
goto Restart
:Arp
echo The arp command is used to display or change entries in the ARP cache.
goto Restart
:Assoc
echo The assoc command is used to display or change the file type associated with a particular file extension.
goto Restart
:At
echo The at command is used to schedule commands and other programs to run at a specific date and time.
goto Restart
:Atmadm
echo The atmadm command is used to display information related to asynchronous transfer mode (ATM) connections on the system.
goto Restart
:Attrib
echo The attrib command is used to change the attributes of a single file or a directory.
goto Restart
:Bootcfg
echo The bootcfg command is used to build, modify, or view the contents of the boot.ini file a hidden file that is used to identify
echo in what folder, on which partition, and on which hard drive Windows is located.
goto Restart
:Break
echo The break command sets or clears extended CTRL+C checking on DOS systems.
goto Restart
:Cacls
echo The cacls command is used to display or change access control lists of files.
goto Restart
:Call
echo The call command is used to to run a script or batch program from within another script or batch program.
goto Restart
:Cd
echo The cd command is the shorthand version of the chdir command. 
goto Restart
:Chcp
echo The chcp command displays or configures the active code page number.
goto Restart
:Chdir
echo The chdir command is used to display the drive letter and folder that you are currently in. Chdir can also
echo be used to change the drive and/or directory that you want to work in.
goto Restart
:Chkdsk
echo The chkdsk command, often referred to as check disk, is used to identify and correct certain hard drive errors.
goto Restart
:Chkntfs
echo The chkntfs command is used to configure or display the checking of the disk drive during the Windows boot process.
goto Restart
:Cipher
echo The cipher command shows or changes the encryption status of files and folders on NTFS partitions.
goto Restart
:Cls
echo The cls command clears the screen of all previously entered commands and other text.
goto Restart
:Cmd
echo The cmd command starts a new instance of the command interpreter.
goto Restart
:Cmstp
echo The cmstp command installs or uninstalls a Connection Manager service profile.
goto Restart
:Color
echo The color command is used to change the colors of the text and background within the Command Prompt window.
goto Restart
:Command
echo The command command starts a new instance of the command.com command interpreter. 
echo The command command is not available in 64-bit versions of Windows XP.
goto Restart
:Comp
echo The comp command is used to compare the contents of two files or sets of files.
goto Restart
:Compact
echo The compact command is used to show or change the compression state of files and directories on NTFS partitions.
goto Restart
:Convert
echo The convert command is used to convert FAT or FAT32 formatted volumes to the NTFS format.
goto Restart
:Copy
echo The copy command does simply that - it copies one or more files from one location to another.
goto Restart
:Cscript
echo The cscript command is used to execute scripts via Microsoft Script Host.
echo The cscript command is most popularly used to manage printers from the command line in Windows XP using scripts
echo like prncnfg.vbs, prndrvr.vbs, prnmngr.vbs, and others.
echo Other popular scripts include eventquery.vbs and pagefileconfig.vbs.
goto Restart
:Date
echo The date command is used to show or change the current date.
goto Restart
:Debug
echo The debug command starts Debug, a command line application used to test and edit programs.
echo The debug command is not available in 64-bit versions of Windows XP.
goto Restart
:Defrag
echo The defrag command is used to defragment a drive you specify. The defrag command is the command line version of Microsoft's Disk Defragmenter.
goto Restart
:Del
echo The del command is used to delete one or more files. The del command is the same as the erase command.
goto Restart
:Diantz
echo The diantz command is used to losslessly compress one or more files. The diantz command is sometimes called Cabinet Maker.
echo The diantz command is the same as the makecab command.
goto Restart
:Dir
echo The dir command is used to display a list of files and folders contained inside the folder that you are currently working in. 
echo The dir command also displays other important information like the hard drive's serial number, the total number of files listed,
echo their combined size, the total amount of free space left on the drive, and more.
goto Restart
:Diskcomp
echo The diskcomp command is used to compare the contents of two floppy disks.
goto Restart
:Diskcopy
echo The diskcopy command is used to copy the entire contents of one floppy disk to another.
goto Restart
:Diskpart
echo The diskpart command is used to create, manage, and delete hard drive partitions.
goto Restart
:Diskperf
echo The diskperf command is used to manage disk performance counters remotely.
goto Restart
:Doskey
echo The doskey command is used to edit command lines, create macros, and recall previously entered commands.
goto Restart
:Dosx
echo The dosx command is used to start DOS Protected Mode Interface (DPMI), 
echo a special mode designed to give MS-DOS applications access to more than the normally allowed 640 KB.
echo The dosx command is not available in 64-bit versions of Windows XP.
echo The dosx command and DPMI is only available in Windows XP to support older MS-DOS programs.
goto Restart
:Driverquery
echo The driverquery command is used to show a list of all installed drivers.
goto Restart
:Echo
echo The echo command is used to show messages, most commonly from within script or batch files.
echo The echo command can also be used to turn the echoing feature on or off.
goto Restart
:Edit
echo The edit command starts the MS-DOS Editor tool which is used to create and modify text files.
echo The edit command is not available in 64-bit versions of Windows XP.
goto Restart
:Edlin
echo The edlin command starts the Edlin tool which is used to create and modify text files from the command line.
echo The edlin command is not available in 64-bit versions of Windows XP.
goto Restart
:Endlocal
echo The endlocal command is used to end the localization of environment changes inside a batch or script file.
goto Restart
:Erase
echo The erase command is used to delete one or more files. The erase command is the same as the del command.
goto Restart
:Esentutl
echo The esentutl command is used to manage Extensible Storage Engine databases.
goto Restart
:Eventcreate
echo The eventcreate command is used to create a custom event in an event log.
goto Restart
:Eventtriggers
echo The eventtriggers command is used to configure and display event triggers.
goto Restart
:Exe2bin
echo The exe2bin command is used to convert a file of the EXE file type (executable file) to a binary file.
echo The exe2bin command is not available in 64-bit versions of Windows XP.
goto Restart
:Exit
echo The exit command is used to end the Command Prompt session that you're currently working in.
goto Restart
:Expand
echo The expand command is used to extract a single file or a group of files from a compressed file.
echo The expand command is not available in 64-bit versions of Windows XP.
goto Restart
:Extrac32
echo The extrac32 command is used to extract the files and folders contained in Microsoft Cabinet (CAB) files.
echo The extrac32 command is actually a CAB extraction program for use by Internet Explorer but can be used to extract
echo any Microsoft Cabinet file. Use the expand command instead of the extrac32 command if possible.
goto Restart
:fastopen
echo The fastopen command is used to add a program's hard drive location to a special list stored in memory, potentially improving 
echo the program's launch time by removing the need for MS-DOS to locate the application on the drive.
echo The fastopen command is not available in 64-bit versions of Windows XP and is only available in 32-bit versions to support older MS-DOS files.
goto Restart
:Fc
echo The fc command is used to compare two individual or sets of files and then show the differences between them.
goto Restart
:Find
echo The find command is used to search for a specified text string in one or more files.
goto Restart
:Findstr
echo The findstr command is used to find text string patterns in one or more files.
goto Restart
:Finger
echo The finger command is used to return information about one or more users on a remote computer that's running the Finger service.
goto Restart
:Fltmc
echo The fltmc command is used to load, unload, list, and otherwise manage Filter drivers.
goto Restart
:For
echo The for command is used to run a specified command for each file in a set of files. The for command is most often 
echo used within a batch or script file.
goto Restart
:Forcedos
echo The forcedos command is used to start the specified program in the MS-DOS subsystem.
echo The forcedos command is not available in 64-bit versions of Windows XP and is only available in 32-bit versions to support 
echo MS-DOS programs that are not recognized as such by Windows XP.
goto Restart
:Format
echo The format command is used to format a drive in the file system that you specify.
echo Drive formatting is also available from Disk Management in Windows XP.
goto Restart
:Fsutil
echo The fsutil command is used to perform various FAT and NTFS file system tasks like managing reparse points and sparse files, 
echo dismounting a volume, and extending a volume. 
goto Restart
:Ftp
echo The ftp command can used to transfer files to and from another computer. The remote computer must be operating as an FTP server.
goto Restart
:Ftype
echo The ftype command is used to define a default program to open a specified file type.
goto Restart
:Getmac
echo The getmac command is used to display the media access control (MAC) address of all the network controllers on a system.
goto Restart
:Goto
echo The goto command is used in a batch or script file to direct the command process to a labeled line in the script.
goto Restart
:Gpresult
echo The gpresult command is used to display Group Policy settings.
goto Restart
:Gpupdate
echo The gpupdate command is used to update Group Policy settings.
goto Restart
:Graftabl
echo The graftabl command is used to enable the ability of Windows to display an extended character set in graphics mode.
echo The graftabl command is not available in 64-bit versions of Windows XP.
goto Restart
:Graphics
echo The graphics command is used to load a program that can print graphics.
echo The graphics command is not available in 64-bit versions of Windows XP.
goto Restart
:Help
echo The help command provides more detailed information on other Command Prompt commands.
goto Restart
:Hostname
echo The hostname command displays the name of the current host. 
goto Restart
:If
echo The if command is used to perform conditional functions in a batch file.
goto Restart
:Ipconfig
echo The ipconfig command is used to display detailed IP information for each network adapter utilizing TCP/IP.
echo The ipconfig command can also be used to release and renew IP addresses on systems configured to receive them via a DHCP server.
goto Restart
:Ipxroute
echo The ipxroute command is used to display and change information about IPX routing tables.
goto Restart
:Kb16
echo The kb16 command is used to support MS-DOS files that need to configure a keyboard for a specific language.
echo The kb16 command is not available in 64-bit versions of Windows XP.
goto Restart
:Label
echo The label command is used to manage the volume label of a disk.
goto Restart
:Loadfix
echo The loadfix command is used to load the specified program in the first 64K of memory and then runs the program.
echo The loadfix command is not available in 64-bit versions of Windows XP.
goto Restart
:Lodctr
echo The lodctr command is used to update registry values related to performance counters.
goto Restart
:Logman
echo The logman command is used to create and manage Event Trace Session and Performance logs. The logman command also supports
echo many functions of Performance Monitor.
goto Restart
:Logoff
echo The logoff command is used to terminate a session.
goto Restart
:Lpq
echo The lpq command displays the status of a print queue on a computer running Line Printer Daemon (LPD). 
goto Restart
:Lpr
echo The lpr command is used to send a file to a computer running Line Printer Daemon (LPD).
goto Restart
:Makecab
echo The makecab command is used to losslessly compress one or more files. The makecab command is sometimes called Cabinet Maker.
echo The makecab command is the same as the diantz command.
goto Restart
:Md
echo The md command is the shorthand version of the mkdir command.
goto Restart
:Mem
echo The mem command shows information about used and free memory areas and programs that are currently loaded into memory in the MS-DOS subsystem.
echo The mem command is not available in 64-bit versions of Windows XP.
goto Restart
:Mkdir
echo The mkdir command is used to create a new folder.
goto Restart
:Mode
echo The mode command is used to configure system devices, most often COM and LPT ports.
goto Restart
:More
echo The more command is used to display the information contained in a text file. 
echo The more command can also be used to paginate the results of any other Command Prompt command.
goto Restart
:Mountvol
echo The mountvol command is used to display, create, or remove volume mount points.
goto Restart
:Move
echo The move command is used to move one or files from one folder to another. The move command is also used to rename directories.
goto Restart
:Mrinfo
echo The mrinfo command is used to provide information about a router's interfaces and neighbors. 
goto Restart
:Msg
echo The msg command is used to send a message to a user.
goto Restart
:Msiexec
echo The msiexec command is used to start Windows Installer, a tool used to install and configure software.
goto Restart
:Nbtstat
echo The nbtstat command is used to show TCP/IP information and other statistical information about a remote computer.
goto Restart
:Net
echo The net command is used to display, configure, and correct a wide variety of network settings.
goto Restart
:Net1
echo The net1 command is used to display, configure, and correct a wide variety of network settings.
echo The net command should be used instead of the net1 command. The net1 command was made available 
echo in versions of Windows before Windows XP as a temporary fix for a Y2K issue that the net command had,
echo which was corrected before the release of Windows XP. The net1 command remains in Windows XP only for compatibility
echo with older programs and scripts that utilized the command.
goto Restart
:Netsh
echo The netsh command is used to start Network Shell, a command-line utility used to manage the network configuration of the local,
echo or a remote, computer. 
goto Restart
:Netstat
echo The netstat command is most commonly used to display all open network connections and listening ports.
goto Restart
:Nlsfunc
echo The nlsfunc command is used to load information specific to a particular country or region.
echo The nlsfunc command is not available in 64-bit versions of Windows XP.
goto Restart
:Nslookup
echo The nslookup is most commonly used to display the hostname of an entered IP address. The nslookup command queries your configured DNS server
echo to discover the IP address.
goto Restart
:Ntbackup
echo The ntbackup command is used to perform various backup functions from the Command Prompt or from within a batch or script file.
goto Restart
:Ntsd
echo The ntsd command is used to perform certain command line debugging tasks.
goto Restart
:Openfiles
echo The openfiles command is used to display and disconnect open files and folders on a system.
goto Restart
:Path
echo The path command is used to display or set a specific path available to executable files.
goto Restart
:Pathping
echo The pathping command functions much like the tracert command but will also report information about network latency and loss at each hop.
goto Restart
:Pause
echo The pause command is used within a batch or script file to pause the processing of the file. When the pause command is used,
echo a Press any key to continue... message displays in the command window.
goto Restart
:Pentnt
echo The pentnt command is used to detect floating point division errors in the Intel Pentium chip.
echo The pentnt command is also used to enable floating point emulation and disable floating point hardware.
goto Restart
:Ping
echo The ping command sends an Internet Control Message Protocol (ICMP) Echo Request message to a specified remote computer 
echo to verify IP-level connectivity.
goto Restart
:Popd
echo The popd command is used to change the current directory to the one most recently stored by the pushd command.
echo The popd command is most often utilized from within a batch or script file.
goto Restart
:Powercfg
echo The powercfg command is used to manage the Windows power management settings from the command line.
goto Restart
:Print
echo The print command is used to print a specified text file to a specified printing device.
goto Restart
:Prompt
echo The prompt command is used to customize the appearance of the prompt text in Command Prompt.
goto Restart
:Pushd
echo The pushd command is used to store a directory for use, most commonly from within a batch or script program.
goto Restart
:Qappsrv
echo The qappsrv command is used to display all Remote Desktop Session Host servers available on the network.
goto Restart
:Qprocess
echo The qprocess command is used to display information about running processes.
goto Restart
:Qwinsta
echo The qwinsta command is used to display information about open Remote Desktop Sessions.
goto Restart
:Rasautou
echo The rasautou command is used to manage Remote Access Dialer AutoDial addresses. 
goto Restart
:Rasdial
echo The rasdial command is used to start or end a network connection for a Microsoft client.
goto Restart
:Rcp
echo The rcp command is used to copy files between a Windows computer and a system running the rshd daemon.
goto Restart
:Rd
echo The rd command is the shorthand version of the rmdir command.
goto Restart
:Recover
echo The recover command is used to recover readable data from a bad or defective disk.
goto Restart
:Reg
echo The reg command is used to manage the Windows Registry from the command line. The reg command can perform common registry functions 
echo like adding registry keys, exporting the registry, etc.
goto Restart
:Regini
echo The regini command is used to set or change registry permissions and registry values from the command line.
goto Restart
:Regsvr32
echo The regsvr32 command is used to register a DLL file as a command component in the Windows Registry.
goto Restart
:Relog
echo The relog command is used to create new performance logs from data in existing performance logs.
goto Restart
:Rem
echo The rem command is used to record comments or remarks in a batch or script file.
goto Restart
:Ren
echo The ren command is the shorthand version of the rename command. 
goto Restart
:Rename
echo The rename command is used to change the name of the individual file that you specify.
goto Restart
:Replace
echo The replace command is used to replace one or more files with one or more other files.
goto Restart
:Reset
echo The reset command, executed as reset session, is used to reset the session subsystem software and hardware to known initial values.
goto Restart
:Rexec
echo The rexec command is used to run commands on remote computers running the rexec daemon.
goto Restart
:Rmdir
echo The rmdir command is used to delete an existing and completely empty folder.
goto Restart
:Route
echo The route command is used to manipulate network routing tables.
goto Restart
:Rsh
echo The rsh command is used to run commands on remote computers running the rsh daemon.
goto Restart
:Rsm
echo The rsm command is used to manage media resources using Removable Storage.
goto Restart
:Runas
echo The runas command is used to execute a program using another user's credentials.
goto Restart
:Rwinsta
echo The rwinsta command is the shorthand version of the reset session command. 
goto Restart
:Sc
echo The sc command is used to configure information about services. The sc command communicates with the Service Control Manager.
goto Restart
:Schtasks
echo The schtasks command is used to schedule specified programs or commands to run a certain times. The schtasks command 
echo can be used to create, delete, query, change, run, and end scheduled tasks.
goto Restart
:Sdbinst
echo The sdbinst command is used to deploy customized SDB database files.
goto Restart
:Secedit
echo The secedit command is used to configure and analyze system security by comparing the current security configuration to a template.
goto Restart
:Set
echo The set command is used to enable or disable certain options in Command Prompt.
goto Restart
:Setlocal
echo  The setlocal command is used to start the localization of environment changes inside a batch or script file.
goto Restart
:Setver
echo The setver command is used to set the MS-DOS version number that MS-DOS reports to a program.
echo The setver command is not available in 64-bit versions of Windows XP.
goto Restart
:Sfc
echo The sfc command is used to verify and replace important Windows system files. The sfc command is also referred to 
echo as System File Checker and Windows Resource Checker.
goto Restart
:Shadow
echo The shadow command Is used to monitor another Remote Desktop Services session.
goto Restart
:Share
echo The share command is used to install file locking and file sharing functions in MS-DOS.
echo The share command is not available in 64-bit versions of Windows XP and is only available in 32-bit versions to support older MS-DOS files.
goto Restart
:Shift
echo The shift command is used to change the position of replaceable parameters in a batch or script file.
goto Restart
:Shutdown
echo The shutdown command can be used to shut down, restart, or log off the current system or a remote computer.
goto Restart
:Sort
echo The sort command is used to read data from a specified input, sort that data, 
echo and return the results of that sort to the Command Prompt screen, a file, or another output device.
goto Restart
:Start
echo The start command is used to open a new command line window to run a specified program or command. 
echo The start command can also be used to start an application without creating a new window.
goto Restart
:Subst
echo The subst command is used to associate a local path with a drive letter. The subst command is a lot like the net use 
echo command except a local path is used instead of a shared network path.
goto Restart
:Systeminfo
echo The systeminfo command is used to display basic Windows configuration information for the local or a remote computer.
goto Restart
:Taskkill
echo The taskkill command is used to terminate a running task. The taskkill command is the command line equivalent of ending a process 
echo in Task Manager in Windows.
goto Restart
:Tasklist
echo Displays a list of applications, services, and the Process ID (PID) currently running on either a local or a remote computer.
goto Restart
:Tcmsetup
echo The tcmsetup command is used to setup or disable the Telephony Application Programming Interface (TAPI) client.
goto Restart
:Telnet
echo The telnet command is used to communicate with remote computers that use the Telnet protocol. 
goto Restart
:Tftp
echo The tftp command is used to transfer files to and from a remote computer that's running the Trivial File Transfer Protocol (TFTP) 
echo service or daemon.
goto Restart
:Time
echo The time command is used to show or change the current time.
goto Restart
:Title
echo The title command is used to set the Command Prompt window title.
goto Restart
:Tlntadmn
echo The tlntadmn command is used to administer a local or remote computer running Telnet Server.
goto Restart
:Tracerpt
echo The tracerpt command is used to process event trace logs or real-time data from instrumented event trace providers.
goto Restart
:Tracert
echo The tracert command is used to show details about the path that a packet takes to a specified destination.
goto Restart
:Tree
echo The tree command is used to graphically display the folder structure of a specified drive or path.
goto Restart
:Tscon
echo The tscon command is used to attach a user session to a Remote Desktop session.
goto Restart
:Tsdiscon
echo The tsdiscon command is used to disconnect a Remote Desktop session.
goto Restart
:Tskill
echo The tskill command is used to end the specified process. 
goto Restart
:Tsshutdn
echo The tsshutdn command is used to remotely shut down or restart a terminal server.
goto Restart
:Type
echo The type command is used to display the information contained in a text file.
goto Restart
:Typeperf
echo The typerperf command displays performance data in the Command Prompt window or writes the data to specified log file.
goto Restart
:Unlodctr
echo The unlodctr command removes Explain text and Performance counter names for a service or device driver from the Windows Registry.
goto Restart
:Ver
echo The ver command is used to display the current Windows version.
goto Restart
:Verify
echo The verify command is used to enable or disable the ability of Command Prompt to verify that files are written correctly to a disk.
goto Restart
:Vol
echo The vol command shows the volume label and serial number of a specified disk, assuming this information exists.
goto Restart
:Vssadmin
echo The vssadmin command starts the Volume Shadow Copy Service administrative command line tool which displays current volume shadow 
echo copy backups and all installed shadow copy writers and providers.
goto Restart
:W32tm
echo The w32tm command is used to diagnose issues with Windows Time.
goto Restart
:Wmic
echo The wmic command starts the Windows Management Instrumentation Command line (WMIC), a scripting interface that simplifies the use of 
echo Windows Management Instrumentation (WMI) and systems managed via WMI.
goto Restart
:Xcopy
echo The xcopy command can copy one or more files or directory trees from one location to another.
goto Restart
:Attrib 
echo The attrib command is used to change the attributes of a single file or a directory
goto restart
:Auditpol 
echo The auditpol command is used to display or change audit policies.
goto restart
:Bcdedit 
echo The bcdedit command is used to view or make changes to Boot Configuration Data.
goto restart
:Bitsadmin 
echo The bitsadmin command is used to create, manage, and monitor download and upload jobs.
goto restart
:Certreq 
echo The certreq command is used to perform various certification authority (CA) certificate functions.
goto restart
:Certutil 
echo The certutil command is used to dump and display certification authority (CA) configuration information in addition to other CA functions.
goto restart
:Change 
echo The change command changes various terminal server settings like install modes, COM port mappings, and logons.
goto restart
:Chcp 
echo The chcp command displays or configures the active code page number.
goto restart
:Chglogon
echo The chglogon command enables, disables, or drains terminal server session logins.
echo The chglogon command is a shortcut to executing change logon.
goto restart
:Chgport
echo The chgport command can be used to display or change COM port mappings for DOS compatibility.
echo The chgport command is a shortcut to executing change port.
goto restart
:Chgusr
echo The chgusr command is used to change the install mode for the terminal server.
echo The chgusr command is a shortcut to executing change user.
goto restart
:Choice 
echo The choice command is used within a script or batch program to provide a list of choices and return of the value of that choice to the program.
goto restart
:Clip
echo The clip command is used to redirect the output from any command to the clipboard in Windows.
goto restart
:Cmdkey
echo The cmdkey command is used to show, create, and remove stored user names and passwords.
goto restart
:Diskraid
echo The diskraid command starts the DiskRAID tool which is used to manage and configure RAID arrays.
goto restart
:Dispdiag
echo The dispdiag command is used to output a log of information about the display system.
goto restart
:Icacls
echo The icacls command is used to display or change access control lists of files. The icacls command is an updated version of the cacls command.
goto restart
:Irftp
echo The irftp command is used to transmit files over an infrared link.
goto restart
:Iscsicli
echo The iscsicli command starts the Microsoft iSCSI Initiator, used to manage iSCSI.
goto restart
:Ktmutil
echo The ktmutil command starts the Kernel Transaction Manager utility.
goto restart
:Mklink
echo The mklink command is used to create a symbolic link.
goto restart
:Mount
echo The mount command is used to mount Network File System (NFS) network shares.
echo The mount command is not available by default in Windows Vista but can be enabled by turning
echo on the Services for NFS Windows feature from Programs and Features in Control Panel.
goto restart
:Muiunattend
echo The muiunattend command starts the Multilanguage User Interface unattended setup process.
goto restart
:Netcfg
echo The netcfg command is used to install the Windows Preinstallation Environment (WinPE), a lightweight version of Windows used to deploy workstations.
goto restart
:Nfsadmin
echo The nfsadmin command is used to manage Server for NFS or Client for NFS from the command line.
echo The nfsadmin command is not available by default in Windows Vista but can be enabled by turning on the Services for NFS Windows feature from Programs and Features in Control Panel.
goto restart
:Ocsetup
echo The ocsetup command starts the Windows Optional Component Setup tool, used to install additional Windows features.
goto restart
:Pkgmgr
echo The pkgmgr command is used to start the Windows Package Manager from the Command Prompt. Package Manager installs, uninstalls, configures, and updates features and packages for Windows.
goto restart
:Pnpunattend
echo The pnpunattend command is used to automate the installation of hardware device drivers.
goto restart
:Pnputil
echo The pnputil command is used to start the Microsoft PnP Utility, a tool used to install a Plug and Play device from the command line.
goto restart
:Query
echo The query command is used to display the status of a specified service.
goto restart
:Quser
echo The quser command is used to display information about users currently logged on to the system.
goto restart
:Robocopy
echo The robocopy command is used to copy files and directories from one location to another.
echo The robocopy command is superior to the more simple copy command because robocopy 
echo supports many more options. This command is also called Robust File Copy.
goto restart
:Rpcinfo
echo The rpcinfo command makes a remote procedure call (RPC) to an RPC server and reports what it finds.
echo The rpcinfo command is not available by default in Windows Vista but can be enabled
echo by turning on the Services for NFS Windows feature from Programs and Features in Control Panel.
goto restart
:Rpcping
echo The rpcping command is used to ping a server using RPC.
goto restart
:Setx
echo The setx command is used to create or change environment variables in the user environment or the system environment.
goto restart
:Showmount
echo The showmount command is used to display information about NFS mounted file systems.
echo The showmount command is not available by default in Windows Vista but can be enabled
echo by turning on the Services for NFS Windows feature from Programs and Features in Control Panel.
goto restart
:Sxstrace
echo The sxstrace command is used to start the WinSxs Tracing Utility, a programming diagnostic tool.
goto restart
:Takeown
echo The takeown command is used to regain access to a file that that an administrator 
echo was denied access to when reassigning ownership of the file.
goto restart
:Telnet
echo The telnet command is used to communicate with remote computers that use the Telnet protocol.
echo The telnet command is not available by default in Windows Vista but can be enabled 
echo by turning on the Telnet Client Windows feature from Programs and Features in Control Panel.
goto restart
:Timeout
echo The timeout command is typically used in a batch or script file to provide a specified timeout 
echo value during a procedure. The timeout command can also be used to ignore keypresses. 
goto restart
:Umount
echo The umount command is used to remove Network File System (NFS) mounted network shares.
echo The umount command is not available by default in Windows Vista but can be enabled 
echo by turning on the Services for NFS Windows feature from Programs and Features in Control Panel.
goto restart
:Waitfor
echo The waitfor command is used to send or wait for a signal on a system.
goto restart
:Wbadmin
echo The wbadmin command is used start and stop backup jobs, display details about a previous backup,
echo list the items within a backup, and report on the status of a currently running backup. 
goto restart
:Wecutil
echo The wecutil command is used to mange subscriptions to events that are forwarded
echo from WS-Management supported computers.
goto restart
:Wevtutil
echo The wevtutil command starts the Windows Events Command Line Utility which is used
echo to manage event logs and publishers.
goto restart
:Where
echo The where command is used to search for files that match a specified pattern.
goto restart
:Whoami
echo The whoami command is used to retrieve user name and group information on a network.
goto restart
:Winrm
echo The winrm command is used to start the command line version of Windows Remote
echo Management, used to manage secure communications with local and remote
echo computers using web services.
goto restart
:Winrs
echo The winrs command is used to open a secure command window with a remote host.
goto restart
:Winsat
echo The winsat command starts the Windows System Assessment
echo Tool, a program that assesses various features, attributes, and
echo capabilities of a computer running Windows.
goto restart
:Wsmanhttpconfig
echo The wsmanhttpconfig command is used to manage aspects of the Windows Remote
echo Management (WinRM) service.
goto restart
:Bcdboot
echo The bcdboot command is used to copy boot files to the system partition and to create a new system BCD store.
goto Restart
:Bdehdcfg
echo The bdehdcfg command is used to prepare a hard drive for BitLocker Drive Encryption.
goto Restart
:Dism
echo The dism command starts the Deployment Image Servicing and Management tool (DISM). The DISM tool is used to manage features in Windows images.
goto Restart
:Forfiles
echo The forfiles command selects one or more files to execute a specified command on. The forfiles command is most often used within a batch or script file.
goto Restart
:Hwrcomp
echo The hwrcomp command is used to compile custom dictionaries for handwriting recognition.
goto Restart
:Hwrreg
echo The hwrreg command is used to install a previously compiled custom dictionary for handwriting recognition.
goto Restart
:Klist
echo The klist command is used to list Kerberos service tickets. The klist command can also be used to purge Kerberos tickets.
goto Restart
:Ksetup
echo The ksetup command is used to configure connections to a Kerberos server.
goto Restart
:Manage-bde
echo The manage-bde command is used to configure BitLocker Drive Encryption from the command line.
goto Restart
:Nltest
echo The nltest command is used to test secure channels between Windows computers in a domain and between domain controllers that are trusting other domains.
echo The nltest command was first available in Windows 7.
goto Restart
:Rdpsign
echo The rdpsign command is used to sign a Remote Desktop Protocol (RDP) file.
goto Restart
:Reagentc
echo The reagentc command is used to configure the Windows Recovery Environment (RE).
goto Restart
:Repair-bde
echo The repair-bde command is used to repair or decrypt a damaged drive that's been encrypted using BitLocker.
goto Restart
:Setspn
echo The setspn command is used to manage the Service Principal Names (SPN) for an Active Directory (AD) service account. 
goto Restart
:Typerperf
echo The typerperf command displays performance data in the Command Prompt window or writes the data to specified log file.
goto Restart
:Tzutil
echo The tzutil command is used to display or configure the current system's time zone. The tzutil command can also be used to enable or disable automatic Daylight Saving Time adjustments.
goto Restart
:Vaultcmd
echo The vaultcmd command is used to create, remove, and show stored credentials.
goto Restart
:Bootsect
echo The bootsect command is used to configure the master boot code to one compatible with Windows 8 (BOOTMGR).
echo The bootsect command is only available from the Command Prompt in System Recovery Options.
goto Restart
:Checknetisolation
echo The checknetisolation command is used to test apps that require network capabilities.
goto Restart
:Djoin
echo The djoin command is used to create a new computer account in a domain.
goto Restart
:Fondue
echo The fondue command, short for Features on Demand User Experience Tool, is used to install any of the several optional Windows 8 features from the command line.
echo Optional Windows 8 features can also be installed from the Programs and Features applet in Control Panel.
goto Restart
:Licensingdiag
echo The licensingdiag command is a tool used to generate a text-based log and other data files that contain product activation and other Windows licensing information.
goto Restart
:Pwlauncher
echo The pwlauncher command is used to enable, disable, or show the status of your Windows To Go startup options.
goto Restart
:Register-cimprovider
echo The register-cimprovider command is used to register a Common Information Model (CIM) Provider in Windows 8.
goto Restart
:Tpmvscmgr
echo The tpmvscmgr command is used to create and destroy TPM virtual smart cards.
goto Restart
:Xwizard
echo The xwizard command, short for Extensible Wizard, is used to register data in Windows, often from a preconfigured XML file.
goto Restart



