import socket

class TCPClient:
    def __init__(self, host, port):
        """
        Initialize the TCPClient with the server's host and port.

        :param host: The server's hostname or IP address.
        :param port: The server's port number.
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect to the TCP server.
        """
        self.socket.connect((self.host, self.port))

    def send_data(self, data):
        """
        Send data to the TCP server.

        :param data: The data to be sent as bytes.
        """
        self.socket.sendall(data)

    def receive_data(self, buffer_size=4096):
        """
        Receive data from the TCP server.

        :param buffer_size: The maximum amount of data to be received at once.
        :return: The received data as bytes.
        """
        return self.socket.recv(buffer_size)

    def close(self):
        """
        Close the connection to the TCP server.
        """
        self.socket.close()
