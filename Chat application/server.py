import socket
import threading

# Function to handle messages from a client
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':
                print("Connection closed.")
                client_socket.close()
                break
            print(f"Client: {message}")
        except:
            break

# Main function to handle server logic
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))  # Binding to localhost and port 12345
    server.listen(1)  # Server will listen for 1 client

    print("Server is listening for incoming connections...")
    client_socket, client_address = server.accept()  # Accept incoming connection
    print(f"Connection established with {client_address}")

    # Start a thread to handle client messages
    threading.Thread(target=handle_client, args=(client_socket,)).start()

    # Main loop for sending messages to the client
    while True:
        message = input("Server: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            client_socket.close()
            break

if __name__ == "__main__":
    start_server()
