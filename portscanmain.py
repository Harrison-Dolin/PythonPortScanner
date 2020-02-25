#!/bin/python3

from datetime import datetime
import sys
import socket

# Target determined for the scan
if len(sys.argv) == 2:
    opnport = socket.gethostbyname(sys.argv[1]) #Hostname
else:
    print("Invalid command.")
    print("Syntax: python3 portscanmain.py <ip address>") #Correct syntax for command given to user
    sys.exit()
    
    
#Startup print statement
print("Scanning target" + opnport) 
print("Time: " + str(datetime.now()))

#Gets range of ports from user
print("\nEnter the range for the scan: ")
lowBound = input("\nEnter lower bound: ")
upperBound = input("\nEnter upper bound: ")

#Valid range check
if lowBound > upperBound or lowBound < 0 or upperBound < 0:
    print("Invalid range")
    sys.exit()
else:
    #Loop to scan all ports within range
    try:
     for prt in range(int(lowBound), int(upperBound)):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        errorHandle = sc.connect_ex((opnport,prt))#Returns error indicator
        if errorHandle == 0: #Check and print for open port
            print("Port {} is open".format(prt))
        sc.close()

    except socket.timeout:
        print("Error: Program time out")
        sys.exit()
        
    except socket.gaierror:
        print("Error: Hostname couldn't be resolved")
        sys.exit()

    except socket.error:
        print("Error: Can't connect to server")
        sys.exit()
    
    except KeyboardInterrupt:
        sys.exit()
