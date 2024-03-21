from socket import *
import sys
import argparse

#Used a modified part of the argparse code from oblig 1:
#Initializing the parser:
parser = argparse.ArgumentParser(description='simple args')

#Adding arguments to the parser:
parser.add_argument('-f' , '--filename', type=str, default="/index.html")
parser.add_argument('-p', '--port', type=int, default=8000) 
parser.add_argument('-i', '--ip', type=str, default="127.0.0.1")

args = parser.parse_args()

#Setting up to test if the IP address is in the correct format
test_ip = args.ip.split(".")
notinrange = False
for number in test_ip:
    if int(number) not in range (0,256): # Assuming we want inclusive 0 and inclusive 255. 
        notinrange = True

#First check for the range of the port, assuming we want inclusive 1024 and inclusive 65535.
if args.port not in range(1024,65536):
    print("Invalid port. It must be within the range [1024,65535]")
#Then check for the format of the IP address. 
#If it doesn't contain 4 numbers or the numbers are out of range you get a error message.
elif len(test_ip)!=4 or notinrange:
    print("Invalid IP. It must in this format: 10.1.2.3")

try:
    #Creating a socket with TCP and a two-way byte stream
    clientSocket = socket(AF_INET,SOCK_STREAM)
    
    #connect to the server and the given IP and Port
    clientSocket.connect((args.ip, args.port))
    
    #Creating a HTTP GET method
    request_header = f"GET / HTTP/1.0\r\nHost: {args.ip}:/{args.port}\r\n{args.filename}\r\n\r\n"
    
    #Sending the GET request to the server
    clientSocket.send(bytes(request_header,"ascii"))
    
    result = ""
    while True:
        #Read data from the socket
        received_line = clientSocket.recv(1024).decode()
        if not received_line:
            break
        result += received_line
    
    #The result is printed to the terminal to easily check it.
    print(result)
    #Closing the client socket and the connection
    clientSocket.close()
    
except error as e:
    print(f"Something happened {e}")