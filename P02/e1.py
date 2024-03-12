from Client0 import Client
print(f"-----| Practice 2, Exercise 1 |------")

IP = "80.58.61.250"  # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()
