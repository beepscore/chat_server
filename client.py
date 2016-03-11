import socket
import sys

HOST, PORT = "localhost", 80

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server and send data
sock.connect((HOST, PORT))

while 1 == 1:
    # In Python 3 use input instead of Python 2 raw_input
    # http://stackoverflow.com/questions/954834/how-do-i-use-raw-input-in-python-3-1
    data = input('--> ')
    sock.send(data + "\n")

# Receive data from the server and shut down
#received = sock.recv(1024)
#sock.close()

#print "Sent:     %s" % data
#print "Received: %s" % received
