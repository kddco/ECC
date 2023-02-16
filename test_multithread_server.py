import socket
import threading

# define a function to handle each client connection
def handle_client(conn, addr):
    print(f"New client connected: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received from client {addr}: {data}")
        conn.sendall(data)
    print(f"Client {addr} disconnected")
    conn.close()

# create a server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific host and port
s.bind(('localhost', 8888))

# listen for incoming connections
s.listen(5)
print("Server is listening on port 8888...")

# accept incoming connections and start a new thread for each connection
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()
