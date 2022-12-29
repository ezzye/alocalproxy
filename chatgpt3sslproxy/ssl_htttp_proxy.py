import socket


# Unit tests

def test_https_proxy():
    proxy = HTTPSProxy()
    assert proxy.host == 'localhost'
    assert proxy.port == 8080


def test_https_proxy_request():
    # Set up a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    # Send a request to the proxy
    request = b'GET / HTTP/1.1\nHost: www.example.com\n\n'
    client_socket.sendall(request)

    # Receive the response from the proxy
    response = client_socket.recv(1024)

    # Verify that the response is correct
    print(request)
    print(response)
    print(response.startswith(b'HTTP/1.1 200 OK'))


test_https_proxy()
test_https_proxy_request()
