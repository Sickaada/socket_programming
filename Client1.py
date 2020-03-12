import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connected to the same port
s.connect((socket.gethostname(),1025))




# save received message from the server
# defining number of bytes in one message..here 1000
'''msg1 = s.recv(1000)
print(msg1.decode("utf-8"))



# taking 1 byte in each iteration.'''
info_received = []
while True:
    msg2 = s.recv(1)
    # client ends after receiving message
    if len(msg2) <= 0:
        break
    info_received.append(msg2.decode("utf-8"))

print(info_received)
