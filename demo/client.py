import socket
# seed the pseudorandom number generator
from random import seed
from random import random

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'Hello, world')
    seed(1)
    while s.recv(1024):
        data = '% .2f' % random()
        s.send(data.encode())
    # data = s.recv(1024)

# print('Received', repr(data))