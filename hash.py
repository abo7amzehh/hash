# -*- coding: utf-8 -*-
P='\033[1;35m'
R='\033[1;31m'
y='\033[1;33m'
import os
import sys
import fileinput
os.system("pkg install nodejs")
os.system("npm install -g bash-obfuscate")
os.system("pkg install figlet")
os.system("clear")



print ("\033[1;33m")
os.system("figlet -f big  Bash")
print ("\033[1;35mThis script caused encryption of bash scripts\n")
Oomd = raw_input(" \033[1;31mnamefile ===>\033[1;35m ")
print ('')
Oomd1 = raw_input(" \033[1;31moutfile ===>\033[1;35m ")

os.system("bash-obfuscate " + Oomd + " -o " + Oomd1)

print ('')
print ("\033[1;35mDone ...")
