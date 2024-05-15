import socket
from urllib.parse import urlparse

class SimpleHTTPClient:
    def __init__(self, url):
        """
        Initialize the SimpleHTTPClient with the URL.

        :param url: The URL to connect to.
        """
        self.url = url
        self.parsed_url = urlparse(url)
        self.host = self.parsed_url.hostname
        self.port = self.parsed_url.port if self.parsed_url.port else 80
        self.path = self.parsed_url.path if self.parsed_url.path else '/'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect to the HTTP server.
        """
        self.socket.connect((self.host, self.port))

    def send_request(self, method="GET", headers=None):
        """
        Send an HTTP request to the server.

        :param method: The HTTP method (e.g., 'GET', 'POST').
        :param headers: Additional headers to include in the request.
        """
        if headers is None:
            headers = {}

        request_line = f"{method} {self.path} HTTP/1.1\r\n"
        host_header = f"Host: {self.host}\r\n"
        additional_headers = ''.join(f"{key}: {value}\r\n" for key, value in headers.items())
        empty_line = "\r\n"

        request = request_line + host_header + additional_headers + empty_line
        self.socket.sendall(request.encode('utf-8'))

    def receive_response(self):
        """
        Receive the HTTP response from the server.

        :return: The HTTP response as a string.
        """
        response = bytearray()
        while True:
            part = self.socket.recv(4096)
            if not part:
                break
            response.extend(part)
        return response.decode('utf-8')

    def close(self):
        """
        Close the connection to the HTTP server.
        """
        self.socket.close()