# Binary Execution

The `brent.binary_execution` package provides tools and utilities for executing and parsing binary files. This package is designed to facilitate the execution of binary files and the extraction of meaningful data from them.

## Modules

The `brent.binary_execution` package includes the following modules:

- `executor.py`: Provides functionality to execute binary files and capture their output.
- `parser.py`: Provides functionality to parse binary files and extract structured data.

## executor.py

### Overview

The `executor.py` module contains the `BinaryExecutor` class, which is used to execute binary files and capture their output.

### BinaryExecutor Class

#### Initialization

```python
BinaryExecutor(binary_path: str)
```

- `binary_path`: The path to the binary file to be executed.

#### Methods

- `execute(input_data: bytes = None) -> str`
  - Executes the binary file and captures its output.
  - `input_data`: Optional input data to be passed to the binary file's standard input.
  - Returns the output of the binary file as a string.

#### Example Usage

```python
from brent.binary_execution.executor import BinaryExecutor

binary_executor = BinaryExecutor('/path/to/binary')
output = binary_executor.execute()
print(f"Binary execution output: {output}")
```

## parser.py

### Overview

The `parser.py` module contains the `BinaryParser` class, which is used to parse binary files and extract structured data.

### BinaryParser Class

#### Initialization

```python
BinaryParser(binary_path: str)
```

- `binary_path`: The path to the binary file to be parsed.

#### Methods

- `parse() -> dict`
  - Parses the binary file and extracts structured data.
  - Returns the parsed data as a dictionary.

#### Example Usage

```python
from brent.binary_execution.parser import BinaryParser

binary_parser = BinaryParser('/path/to/binary')
parsed_data = binary_parser.parse()
print(f"Parsed binary data: {parsed_data}")
```

## Detailed Descriptions

### BinaryExecutor

The `BinaryExecutor` class provides a simple interface to execute binary files and capture their output. It supports optional input data that can be passed to the binary file's standard input. This class is useful for scenarios where you need to automate the execution of binary files and process their output programmatically.

### BinaryParser

The `BinaryParser` class provides functionality to parse binary files and extract structured data. This class is useful for scenarios where you need to analyze the contents of binary files and convert them into a more usable format, such as a dictionary.

## Notes

- Ensure that the binary files you intend to execute or parse are accessible and have the necessary permissions.
- The `BinaryExecutor` class captures the standard output of the binary file. If the binary file writes output to a different stream, additional handling may be required.
- The `BinaryParser` class assumes a specific format for the binary file. Modify the parsing logic as needed to suit the format of your binary files.


### Explanation

- **Modules**: Describes the modules in the `brent.binary_execution` package.
- **executor.py**: Provides an overview and detailed description of the `BinaryExecutor` class, including its initialization, methods, and example usage.
- **parser.py**: Provides an overview and detailed description of the `BinaryParser` class, including its initialization, methods, and example usage.
- **Detailed Descriptions**: Elaborates on the functionality and use cases of the `BinaryExecutor` and `BinaryParser` classes.
- **Notes**: Provides additional information and considerations for using the classes in the `brent.binary_execution` package.