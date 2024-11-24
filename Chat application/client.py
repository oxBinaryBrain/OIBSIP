import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':
                print("Connection closed by server.")
                client_socket.close()
                break
            print(f"Server: {message}")
        except:
            break

# Main function to handle client logic
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))  # Connect to server at localhost on port 12345

    # Start a thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client,)).start()

    # Main loop for sending messages to the server
    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            client.close()
            break

if __name__ == "__main__":
    start_client()
