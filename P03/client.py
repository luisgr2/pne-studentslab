import socket


class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def __str__(self):
        return f"Connection to SERVER at {self.server_ip}, PORT: {self.server_port}"

    def ping(self):
        print("OK")

    def talk(self, msg):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.server_ip, self.server_port))
        msg_bytes = str.encode(msg)
        client_socket.send(msg_bytes)
        response_bytes = client_socket.recv(2048)
        response = response_bytes.decode()
        client_socket.close()
        return response