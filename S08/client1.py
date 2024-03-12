import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
SERVER_PORT = 8081
SERVER_IP = "127.0.0.1" # it depends on the machine the server is running

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((SERVER_IP, SERVER_PORT))

# Send data. No strings can be sent, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("quiero colacao"))

# Close the socket
s.close()
