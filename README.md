# Data2410oblig2
## Task 1: Making a simple webserver
Used the skeleton code and changed it into a web server. When writing 127.0.0.1:8000/index.html, the index.html file in the folder is rendered. 
![image](https://github.com/eirinko/data2410oblig2/assets/31256905/ed6901c1-a232-430b-be0c-5f470408c259)

When calling for another page, for example, 127.0.0.1:8000/dex.html a 404 error is shown. 
![image](https://github.com/eirinko/data2410oblig2/assets/31256905/b54243eb-9e04-4289-908c-12b034323f02)

## Task 2: Making a web client
For adding the arguments in the terminal some of the code from oblig 1 was used (for argparse), but with modifications to fit this task. All the arguments have default values and the file can be run without adding arguments. If the arguments are invalid, the client will get a 404 Not Found error. For examples of how the client works, have a look at the picture below:
![image](https://github.com/eirinko/data2410oblig2/assets/31256905/6039e630-90ff-440c-ad1a-44cdd5c6fe06)

For the rest of the code: the client connects to the IP and port given and sends an HTTP GET request to the server. All the information it gets from the server is added to a result that is printed before closing the socket. 

## Task 3: Making a multi-threaded web server
Running the multi-threaded server and then running two clients will yield this result:
![image](https://github.com/eirinko/data2410oblig2/assets/31256905/e4d67f96-d2c8-41d8-8151-b6616f438630)
The first client is connected to port 47586 and the second is connected to 47594.
