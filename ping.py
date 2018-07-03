#!/usr/bin/python3.6
import subprocess
#subprocess.call('ls -ltr',shell=True)
#output = subprocess.check_output('ls',shell=True)
#print(output)
#print(hostname)
import subprocess as sp

def ipcheck():
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
    print(result)
    print(status)
    if status == 0:
        print("System " + str(pop) + " is UP !")
    else:
        print("System " + str(pop) + " is DOWN !")


pop = input("Enter the ip address: ")
ipcheck()
