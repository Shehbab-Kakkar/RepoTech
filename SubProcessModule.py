#!/usr/bin/python3.6
import subprocess
#Good view of shell commmands as it is

subprocess.call('ls -l | grep -i file',shell=True)

#Ugly view of shell commands in a single line.

print(subprocess.check_output('ls -l | grep -i file',shell=True))

#######################
