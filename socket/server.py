# server.py

import socket  # Import socket module

port = 50000  # Reserve a port for your service.
s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
print("Host:", host)
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

print("Server listening....")

while True:
    conn, addr = s.accept()  # Establish connection with client.
    print("Got connection from", addr)
    data = conn.recv(1024)
    print("Server received: ", data.decode("utf-8"))

    filename = "mytext.txt"
    with open(filename, "rb") as f:
        l = f.read(1024)
        while l:
            conn.send(l)
            print("Sent ", repr(l))
            l = f.read(1024)

    print("Done sending")
    conn.send("Thank you for connecting".encode("utf-8"))
    conn.close()
