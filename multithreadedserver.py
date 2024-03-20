#import socket module
from socket import *
import sys # In order to terminate the program
import _thread as thread

def handleClient(connection):
    while True:
        #Receiving message from the client
        message = connection.recv(1024).decode()
        print(message)
        filename = message.split('\r\n')[2]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header into socket
        encoding = 'ascii'
        connection.send(bytes('HTTP/1.0 200 OK\r\n', encoding))
        connection.send(bytes('Content-Type: text/html\r\n\r\n', encoding))

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connection.send(outputdata[i].encode()) 
        connection.send("\r\n".encode())
        
    #Close client socket
    connection.close()

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
        
        #Added to create threads for many clients
        while True:
            connectionSocket, addr = serverSocket.accept()
            print("Server connected to ",addr)
            thread.start_new_thread(handleClient,(connectionSocket,))

    except IOError:
        #Send response message for file not found
        encoding = 'ascii'
        connectionSocket.send(bytes('HTTP/1.0 404 Not Found\r\n', encoding))
        
        #Close client socket
        connectionSocket.close()
        
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data