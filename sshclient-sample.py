#!/usr/bin/python3.6
import paramiko
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect("server.example.com",port =22, username = "username", password="passwd")
stdin, stdout, stderr = p.exec_command("ls -l /home/test")
#opterr = stderr.readlines()
print()
optout = stdout.readlines()  # Convert the output into list
#optout = stderr.readlines()  # Convert the output into list
print(optout)
print()
opt ="".join(optout)  #Joining the list to convert it into a readable format
print(opt)
