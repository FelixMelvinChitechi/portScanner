#!/bin/python3

import sys
import socket
from datetime import datetime


#Define our target
if len(sys.argv) == 2:
     target = socket.gethostbyname(sys.argv[1]) # Translating a host name to IPv4
     
else:
     print("Invalid amount of arguments.")
     print("syntax: python3 scanner.py <ip>")
         
#Add a pretty banner
print("_" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("_" * 50)

try:
	
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # returns an error indicator 
		print("Checking port {}".format(port))
		if result == 0:
			print("port {} is open".format(port))
                  
	s.close()
             
except KeyboardInterrupt: 
          print("\nExiting program.")
          sys.exit()
          
except socketsocket.gaierror:
          print("Hostname could not be resolved.")
          sys.exit()
          
except socket.error:
          print("couldn't connect to server")
          sys.exit()
          
                  
            

