import socket 
import sys 
import os 

server_address = '/tmp/mysocket' 
# Make sure the socket does not already exist 
try: 
    os.unlink(server_address) 
except OSError: 
    if os.path.exists(server_address):
        raise 

# Create a UDS socket 
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) 

# Bind the socket to the port 
print >>sys.stderr, 'starting up on %s' % server_address 
sock.bind(server_address) 

while True: 
    # Wait for a connection 
    print >>sys.stderr, 'waiting for a connection' 
    print >>sys.stderr, 'connection from' 

    # Receive the data in small chunks and retransmit it 
    while True: 
        data = sock.recv(16) 
        print >>sys.stderr, 'received "%s"' % data 
        if data: 
            print >>sys.stderr, 'sending data back to the client'
        else: 
            print >>sys.stderr, 'no more data from' 
            break
