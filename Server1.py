import socket
# create socket using module
# AF_INET: address ; SOC_STREAM: Create IP/TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# taking two parameter:(host and port number in tuple)
# gethostname is used when server as well as client are on same pc 
s.bind((socket.gethostname(),1025))
s.listen(5)
while True:
# accepting my client 
    clt,adr = s.accept()
    print(f"connection to {adr} established")
# passing some message to the client after establishment of connection
    clt.send(bytes("socket programming in Python","utf-8"))  
    # closing server
    clt.close()  
