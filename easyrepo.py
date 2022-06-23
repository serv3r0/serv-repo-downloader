#! /usr/bin/python

import os
# import time
import enquiries

os.system ( "clear" )
print ( "    ______                 ______               " )
print ( "   / ____/___ ________  __/ __  /___  ____  ____ " )
print ( "  / __/ / __ `/ ___/ / / / /_/ / _  / __  / __  " )
print ( " / /___/ /_/ (__  ) /_/ / _, _/  __/ /_/ / /_/ /" )
print ( "/_____/___,_/____/___, /_/ |_|____/ .___/ ____/ " )
print ( "                 /____/          /_/            " )
print ( " " )

options = ['Download' , 'Exit']
choice = enquiries.choose ( 'Choose one of the options below: ' , options )

# Download Category start

if choice == ('Download') :
    doptions = ['Arch App Installer (Shell Script)' , 'Auto Qemu Installer (Shell Script)' ,
                'Auto Unreal Engine 5 (Shell Script)'
        , 'Easy Minecraft Server Installer (Shell Script)' , 'Exit']
    dchoice = enquiries.choose ( 'Choose one of the options below: ' , doptions )

# Shell Scripts start

if dchoice == ('Arch App Installer (Shell Script)') :
    os.system ( 'git clone https://github.com/serv3r0/arch-app-inst.git' )
    print (
        'now you can cd into the directory, to make sh executable use "chmod +x appinst.sh" and then to launch it use "./appinst.sh"' )

if dchoice == ('Auto Qemu Installer (Shell Script)') :
    os.system ( 'https://github.com/serv3r0/autoqemu.git' )
    print (
        'now you can cd into the directory, to make sh executable use "chmod +x autoqemu.sh" and then to launch it use "./autoqemu.sh"' )

if dchoice == ('Auto Unreal Engine 5 (Shell Script)') :
    os.system ( 'git clone https://github.com/serv3r0/autoue5.git' )
    print (
        'now you can cd into the directory, to make sh executable use "chmod +x autoue5.sh" and then to launch it use "./autoue5.sh' )

if dchoice == ('Easy Minecraft Server Installer (Shell Script)') :
    os.system ( 'git clone https://github.com/serv3r0/emcs.git' )
    print (
        'now you can cd into the directory, to make sh executable use "chmod +x emcs.sh" and then to launch it use "./emcs.sh' )

# Shell Scripts end

if dchoice == ('Exit') :
    exit ()

# Download Category end

if choice == ('Exit') :
    print ( 'bye' )
exit ()
