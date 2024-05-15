import socket
import struct

class CustomProtocol:
    HEADER_FORMAT = '!I'  # Example header format: 4-byte unsigned int
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

    def __init__(self, host, port):
        """
        Initialize the CustomProtocol with the server's host and port.

        :param host: The server's hostname or IP address.
        :param port: The server's port number.
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect to the server.
        """
        self.socket.connect((self.host, self.port))

    def send_message(self, message):
        """
        Send a message to the server using the custom protocol.

        :param message: The message to be sent as a string.
        """
        encoded_message = message.encode('utf-8')
        header = struct.pack(self.HEADER_FORMAT, len(encoded_message))
        self.socket.sendall(header + encoded_message)

    def receive_message(self):
        """
        Receive a message from the server using the custom protocol.

        :return: The received message as a string.
        """
        header = self._recv_n_bytes(self.HEADER_SIZE)
        if not header:
            return None
        message_length = struct.unpack(self.HEADER_FORMAT, header)[0]
        message = self._recv_n_bytes(message_length)
        return message.decode('utf-8')

    def close(self):
        """
        Close the connection to the server.
        """
        self.socket.close()

    def _recv_n_bytes(self, n):
        """
        Receive exactly n bytes from the socket.

        :param n: Number of bytes to receive.
        :return: The received bytes.
        """
        data = bytearray()
        while len(data) < n:
            packet = self.socket.recv(n - len(data))
            if not packet:
                return None
            data.extend(packet)
        return bytes(data)
