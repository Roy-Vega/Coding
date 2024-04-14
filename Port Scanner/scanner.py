#!/bin/python3

import sys
import socket
from datetime import datetime

#Define out target
if len(sys.argv) == 2: #"argv" is number of arguments
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")

#Banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85): #range of ports
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #we get IP and port
		socket.setdefaulttimeout(1) #if it doesn't respond back, within a sec move on
		result = s.connect_ex((target,port)) #'target' is argument typed 'port' changes with loop
		if result == 0: #error result returns 0 if port open
			print(f"Port {port} is open")
			s.close() #we close it and try again

except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Could not connect to the server")
	sys.exit()

