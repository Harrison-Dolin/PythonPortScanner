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


try:
    for prt in range(45, 80):
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
