# Network

The `brent.network` package provides tools and utilities for managing network tasks and protocols. This package is designed to facilitate the scheduling of network tasks and the implementation of various network protocols.

## Modules

The `brent.network` package includes the following modules:

- `scheduler.py`: Provides functionality to schedule and manage network tasks.
- `protocols/`: Contains implementations of different network protocols.

## scheduler.py

### Overview

The `scheduler.py` module contains the `NetworkTaskScheduler` class, which is used to schedule and manage network tasks.

### NetworkTaskScheduler Class

#### Initialization

```python
NetworkTaskScheduler()
```

#### Methods

- `add_task(priority: int, task_id: str, action: Callable, *args, **kwargs)`
  - Adds a task to the scheduler with a specified priority.
  - `priority`: The priority of the task (lower number means higher priority).
  - `task_id`: A unique identifier for the task.
  - `action`: The function to be executed as the task.
  - `args`: Positional arguments to pass to the action.
  - `kwargs`: Keyword arguments to pass to the action.

- `stop()`
  - Stops the scheduler and waits for the worker thread to finish.

- `get_task_count() -> int`
  - Returns the number of tasks in the scheduler.

#### Example Usage

```python
from brent.network.scheduler import NetworkTaskScheduler

scheduler = NetworkTaskScheduler()

def example_task(task_id):
    print(f"Running task {task_id}")

scheduler.add_task(priority=1, task_id="task1", action=example_task, task_id="task1")
scheduler.add_task(priority=2, task_id="task2", action=example_task, task_id="task2")
scheduler.add_task(priority=0, task_id="task3", action=example_task, task_id="task3")

# Run the scheduler for a short period to process the tasks
import time
time.sleep(2)
scheduler.stop()
```

## protocols/custom_protocol.py

### Overview

The `custom_protocol.py` module contains the `CustomProtocol` class, which implements a custom network protocol.

### CustomProtocol Class

#### Initialization

```python
CustomProtocol(host: str, port: int)
```

- `host`: The server's hostname or IP address.
- `port`: The server's port number.

#### Methods

- `connect()`
  - Connects to the server.

- `send_message(message: str)`
  - Sends a message to the server.
  - `message`: The message to be sent.

- `receive_message() -> str`
  - Receives a message from the server.
  - Returns the received message as a string.

- `close()`
  - Closes the connection to the server.

#### Example Usage

```python
from brent.network.protocols.custom_protocol import CustomProtocol

client = CustomProtocol('localhost', 12345)
client.connect()
client.send_message("Hello, server!")
response = client.receive_message()
print(f"Received: {response}")
client.close()
```

## protocols/http.py

### Overview

The `http.py` module contains the `SimpleHTTPClient` class, which provides a simple HTTP client for making HTTP requests.

### SimpleHTTPClient Class

#### Initialization

```python
SimpleHTTPClient(url: str)
```

- `url`: The URL to connect to.

#### Methods

- `connect()`
  - Connects to the HTTP server.

- `send_request(method: str = "GET", headers: dict = None)`
  - Sends an HTTP request to the server.
  - `method`: The HTTP method (e.g., 'GET', 'POST').
  - `headers`: Additional headers to include in the request.

- `receive_response() -> str`
  - Receives the HTTP response from the server.
  - Returns the HTTP response as a string.

- `close()`
  - Closes the connection to the HTTP server.

#### Example Usage

```python
from brent.network.protocols.http import SimpleHTTPClient

client = SimpleHTTPClient("http://example.com")
client.connect()
client.send_request()
response = client.receive_response()
print(response)
client.close()
```

## protocols/tcp.py

### Overview

The `tcp.py` module contains the `TCPClient` class, which provides a simple TCP client for communicating with a TCP server.

### TCPClient Class

#### Initialization

```python
TCPClient(host: str, port: int)
```

- `host`: The server's hostname or IP address.
- `port`: The server's port number.

#### Methods

- `connect()`
  - Connects to the TCP server.

- `send_data(data: bytes)`
  - Sends data to the TCP server.
  - `data`: The data to be sent as bytes.

- `receive_data(buffer_size: int = 4096) -> bytes`
  - Receives data from the TCP server.
  - `buffer_size`: The maximum amount of data to be received at once.
  - Returns the received data as bytes.

- `close()`
  - Closes the connection to the TCP server.

#### Example Usage

```python
from brent.network.protocols.tcp import TCPClient

client = TCPClient("localhost", 12345)
client.connect()
client.send_data(b"Hello, server!")
response = client.receive_data()
print(f"Received: {response}")
client.close()
```

## Notes

- Ensure that the network services you intend to connect to are running and accessible.
- The `NetworkTaskScheduler` class runs tasks in a separate thread. Proper thread management should be ensured to avoid unexpected behavior.
- The protocol classes (`CustomProtocol`, `SimpleHTTPClient`, `TCPClient`) are basic implementations and may need to be extended for more complex use cases.

### Explanation

- **Modules**: Lists the modules included in the `brent.network` package.
- **scheduler.py**: Provides an overview and detailed description of the `NetworkTaskScheduler` class, including its initialization, methods, and example usage.
- **protocols/custom_protocol.py**: Provides an overview and detailed description of the `CustomProtocol` class, including its initialization, methods, and example usage.
- **protocols/http.py**: Provides an overview and detailed description of the `SimpleHTTPClient` class, including its initialization, methods, and example usage.
- **protocols/tcp.py**: Provides an overview and detailed description of the `TCPClient` class, including its initialization, methods, and example usage.
- **Notes**: Provides additional information and considerations for using the classes in the `brent.network` package.