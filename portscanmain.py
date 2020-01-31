#!/bin/python3

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

if lowBound > upperBound or lowBound < 0 or upperBound < 0:
    print("Invalid range")
else:
    
    try:
     for prt in range(lowBound, upperBound):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        errorHandle = sc.connect_ex((opnport,prt))#Returns error indicator
        if errorHandle == 0:
            print("Port {} is open".format(prt))
        sc.close()

    except socket.gaierror:
        print("Hostname couldn't be resolved")
        sys.exit()

    except socket.error:
        print("Can't connect to server")
        sys.exit()
    
    except KeyboardInterrupt:
        sys.exit()
