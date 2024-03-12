from Client0 import Client
print(f"-----| Practice 2, Exercise 3 |------")
IP = "192.168.0.33"
PORT = 8081
c = Client(IP, PORT)
print(c)
print("Sending a message to the server...")
response = c.talk("quiero colacao")
print(f"Response: {response}")
