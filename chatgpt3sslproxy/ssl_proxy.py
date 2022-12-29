import ssl
import socket
import threading


class HTTPSProxy:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port

        # Set up a socket to listen for incoming connections
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.bind((self.host, self.port))
        self.listen_socket.listen()

    def start(self):
        while True:
            # Accept a new connection
            client_socket, client_address = self.listen_socket.accept()
            # Handle the connection in a new thread
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        # Get the request from the client
        request = client_socket.recv(1024)
        print(f'Request: {request}')

        # Extract the hostname from the request
        hostname = self.get_hostname(request)
        print(f'Hostname: {hostname}')

        # Connect to the target server
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((hostname, 443))

        # Wrap the target socket with an SSL layer
        target_socket = ssl.wrap_socket(target_socket)

        # Forward the request to the target server
        target_socket.sendall(request)

        # Get the response from the target server
        response = target_socket.recv(1024)
        print(f'Response: {response}')

        # Send the response back to the client
        client_socket.sendall(response)

        # Clean up
        client_socket.close()
        target_socket.close()

    def get_hostname(self, request):
        # Parse the request to extract the hostname
        # (Assumes the request is well-formed)
        lines = request.split(b'\n')
        host_header = [l for l in lines if l.startswith(b'Host:')][0]
        hostname = host_header.split(b' ')[1]
        return hostname.strip()


def test_https_proxy():
    proxy = HTTPSProxy()
    print('Proxy started')
    proxy.start()


test_https_proxy()
