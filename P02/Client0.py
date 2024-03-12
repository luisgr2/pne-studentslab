class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        connection = f"Connection to SERVER at {self.ip}, PORT: {self.port}"
        return connection

    def ping(self):
        print("OK")

    def talk(self, msg):
        import socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))
        client_socket.send(str.encode(msg))
        response = client_socket.recv(2048).decode("utf-8")
        client_socket.close()
        return response
