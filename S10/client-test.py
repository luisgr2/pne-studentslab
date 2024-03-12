from Client0 import Client

SERVER_IP = "localhost"
SERVER_PORT = 8080
MESSAGES = 5

c = Client(SERVER_IP, SERVER_PORT)
for i in range(MESSAGES):
    c.talk(f"Message {i}")