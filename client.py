from socket import *
import sys
import argparse


try:
    clientSocket = socket(AF_INET,SOCK_STREAM)
    
    port = 8000
    server_ip = '127.0.0.1'
    
    #connect to the server
    clientSocket.connect((server_ip, port)) #IP and port in tuple.
    
    inp=""
    while (inp.lower() != "exit"):
        inp = input("Connected to the server. Enter the file name: ")
        print('Your input: ',inp)
        
        #Send data:
        clientSocket.send(inp.encode())
        
        #Read data from the socket
        #What happens when there are several lines????
        received_line = clientSocket.recv(1024).decode()
        
        #prints
        print(received_line)
    
    clientSocket.close()
    
except error as e:
    print(f"Something happened {e}")