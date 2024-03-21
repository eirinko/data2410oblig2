#import socket module
from socket import *
import sys # In order to terminate the program
import _thread as thread

#Function for handling each client thread:
def handleClient(connection):
    #Receiving message from the client
    message = connection.recv(1024).decode()
    
    #The file name is the info on index 2.
    filename = message.split('\r\n')[2]
    
    #Opening the file (in this case: index.html) and reading it to output data
    f = open(filename[1:])
    outputdata = f.read()

    #Send an HTTP header into the socket
    connection.send(bytes('HTTP/1.0 200 OK\r\n', 'ascii'))
    connection.send(bytes('Content-Type: text/html\r\n\r\n', 'ascii'))

    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
        connection.send(outputdata[i].encode()) 
    #Close client socket
    connection.close()

#Creating a socket with TCP and a two-way byte stream
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a info for server socket to listen for clients
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
        connectionSocket.send(bytes('HTTP/1.0 404 Not Found\r\n', 'ascii'))
        
        #Close client socket
        connectionSocket.close()
        
serverSocket.close() #The server runs indefinitely, until killed in the terminal
sys.exit()#Terminate the program after sending the corresponding data