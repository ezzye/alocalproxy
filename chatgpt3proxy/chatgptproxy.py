import socket
import threading

# Set up a socket to listen for incoming connections
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(('localhost', 8080))
listen_socket.listen()


# A function to handle incoming connections
def handle_client(client_socket):
    # Get the request from the client
    request = client_socket.recv(1024)

    # Forward the request to the target server
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect(('www.example.com', 80))
    target_socket.sendall(request)

    # Get the response from the target server
    response = target_socket.recv(1024)

    # Send the response back to the client
    client_socket.sendall(response)

    # Clean up
    client_socket.close()
    target_socket.close()


while True:
    # Accept a new connection
    client_socket, client_address = listen_socket.accept()
    # Handle the connection in a new thread
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
