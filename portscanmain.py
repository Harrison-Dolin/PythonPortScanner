#!/bin/python

import sys
import socket
from datetime import datetime

# Target determined for the scan
if len(sys.argv) == 2:
    opnport = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid command.")
    print("Syntax: python3 portscanmain.py <ip address>")
    
    

print("Scanning target" + opnport)
print("Time: " + str(datetime.now()))


print("\nEnter the range for the scan: ")
lowBound = input("\nEnter lower bound: ")
upperBound = input("\nEnter upper bound: ")

try:
    for prt in range(lowBound, upperBound):
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            errorHandle = s.connect_ex((opnport,prt))#Returns error indicator
            if errorHandle == 0:
                print("Port {} is open".format(prt))
            s.close()

except socket.gaierror:
    print("Hostname couldn't be resolved")
    sys.exit()

except socket.error:
    print("Can't connect to server")
    sys.exit()
    
except KeyboardInterrupt:
    sys.exit()
