# Socket Server Implementation TCP69

This script implements a basic server-client communication using Python's `socket` module. It is designed to:
- Handle two client connections.
- Allow clients to select and exchange choices (e.g., hero selection in a game).
- Facilitate continuous communication between the connected clients.

## Features

1. **Server Binding**:
   - Initializes a server socket.
   - Binds the server to a specified IP and port.

2. **Client Handling**:
   - Listens for incoming client connections.
   - Accepts and manages two client connections simultaneously.

3. **Data Exchange**:
   - Receives a selection from one client and forwards it to the other.
   - Continuously facilitates communication between the two clients.

## How to Use

### Prerequisites

- Python 3 installed on your system.
- Basic understanding of networking and IP addresses.

### Steps

1. Save the script as `socket_server.py` or any name that you want.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python socket_server.py
   ```

### Example Execution

1. **Server Start**:
   - The server binds to the host IP and port (default: 5050).
   - Waits for two client connections.
   ```bash
   [$] server binded
   [$] server listening on 192.168.1.100
   [*] waiting for connection....
   ```

2. **Client Connection**:
   - The server displays the IP and connection details of connected clients.
   ```bash
   [$] ('192.168.1.101', 50000) has been connected with connection: <socket.socket fd=3>
   [$] ('192.168.1.102', 50001) has been connected with connection: <socket.socket fd=4>
   ```

3. **Hero Selection and Exchange**:
   - Clients choose a hero, and their selections are exchanged.
   ```bash
   waiting for client to select
   ('192.168.1.101', 50000) choose Warrior
   waiting for client to select
   ('192.168.1.102', 50001) choose Mage
   ```

4. **Continuous Communication**:
   - The server facilitates back-and-forth data exchange between the clients.

## Script Breakdown

- **`binding()`**:
  - Binds the server to the specified address and port.
  - Displays a success message if binding is successful.

- **`start()`**:
  - Starts listening for client connections.
  - Handles errors gracefully if the server fails to start.

- **`accepting()`**:
  - Accepts and manages two client connections.
  - Displays connection details for both clients.

- **`receiving_hero(recv_addr, send_addr)`**:
  - Receives a hero selection from one client.
  - Sends the selection to the other client.

- **`sendchoose(c1, c2)`**:
  - Receives data from one client and forwards it to the other.

- **Main Execution**:
  - The server binds, starts, and accepts connections.
  - Facilitates hero selection and continuous communication.

## Notes

- Default IP and Port: The server uses the host machine's IP and port `5050`. Modify the `PORT` variable to change the port.
- Ensure the clients are on the same network as the server or have proper routing configured.
- This script is designed for learning purposes and may require enhancements for production use.

