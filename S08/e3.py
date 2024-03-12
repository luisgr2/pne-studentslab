import socket

# SERVER IP, PORT
PORT = 2024
IP = "127.0.0.1"  # depends on the computer the server is running
while ok:

    # -- Ask the user for the message
    message = input("Client:")
    # -- Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- Establish the connection to the Server
    client_socket.connect((IP, PORT))
    # -- Send the user message
    client_socket.send(str.encode(message))
    # -- Close the socket
    client_socket.close()