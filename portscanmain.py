#!/bin/python

import sys
import socket
from datetime import datetime

#Define the target for the scan
if len(sys.argv) == 2:
    #Converting host name to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid arguemnt count.")
    print("Syntax: python3 portscanmain.py <ip address>")

#Include a banner
print("-" * 50)
print("Scanning target" + target)
print("Time: " + str(datetime.now()))
print("-" * 50)

print("\nEnter the range for the scan: ")
lowBound = input("\nEnter lower bound: ")
upperBound = input("\nEnter upper bound: ")

try:
    for port in range(lowBound, upperBound):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))#Returns error indicator
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

except KeyboardInterrupt:
    print("\nExit program")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved")
    sys.exit()

except socket.error:
    print("Can't connect to server")
    sys.exit()