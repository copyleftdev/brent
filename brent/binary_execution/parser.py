import struct

class BinaryParser:
    def __init__(self, binary_path):
        """
        Initialize the BinaryParser with the path to the binary file.

        :param binary_path: Path to the binary file to be parsed.
        """
        if not os.path.isfile(binary_path):
            raise FileNotFoundError(f"The binary file '{binary_path}' does not exist.")
        self.binary_path = binary_path

    def parse(self):
        """
        Parse the binary file and return the parsed data.

        :return: Parsed data from the binary file.
        """
        parsed_data = {}
        with open(self.binary_path, 'rb') as binary_file:
            # Example: Parse the first 4 bytes as an integer
            parsed_data['header'] = struct.unpack('I', binary_file.read(4))[0]
            # Example: Parse the next 8 bytes as a double
            parsed_data['value'] = struct.unpack('d', binary_file.read(8))[0]
            # Example: Parse the next 16 bytes as a string
            parsed_data['name'] = binary_file.read(16).decode('utf-8').strip('\x00')
        return parsed_data

    def parse_section(self, offset, size, fmt):
        """
        Parse a specific section of the binary file.

        :param offset: Offset in the binary file to start reading from.
        :param size: Number of bytes to read from the offset.
        :param fmt: Format string for struct.unpack to parse the data.
        :return: Parsed data from the specified section.
        """
        with open(self.binary_path, 'rb') as binary_file:
            binary_file.seek(offset)
            section_data = binary_file.read(size)
            parsed_section = struct.unpack(fmt, section_data)
        return parsed_section

