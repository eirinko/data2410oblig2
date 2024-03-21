#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a server socket
server_port = 8000
server_ip = '127.0.0.1'
serverSocket.bind((server_ip, server_port))
serverSocket.listen(1)

while True:
    #Establish the connection print('Ready to serve...') connectionSocket, addr = 
    try:
        print("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        
        #Receiving message from the client
        message = connectionSocket.recv(1024).decode()
        
        #File to be opened
        filename = message.split('\r\n')[2]
        
        #Opening the file and reading it to outputdata
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header into socket
        encoding = 'ascii'
        connectionSocket.send(bytes('HTTP/1.0 200 OK\r\n', encoding))
        connectionSocket.send(bytes('Content-Type: text/html\r\n\r\n', encoding))

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode())
        
        #Close client socket
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        encoding = 'ascii'
        connectionSocket.send(bytes('HTTP/1.0 404 Not Found\r\n', encoding))
        
        #Close client socket
        connectionSocket.close()
        
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data