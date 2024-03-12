from client import Client

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080
N = 5

sequence = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"] #list to iterate through in a loop
print("-----| Practice 3, Exercise 7 |------")

c = Client(SERVER_IP, SERVER_PORT)
print(c)
print("* Testing PING...")
response = c.talk("PING")
print(response)

print("* Testing GET...")
for n in range(N):
    response = c.talk(f"GET {n}")
    print(f"Get {n}: {response}")

print("* Testing INFO...")
response = c.talk(f"INFO {sequence}")
print(response)

print("* Testing COMP...")
print(f"COMP {sequence}")
response = c.talk(f"COMP {sequence}")
print(response)

print("* Testing REV...")
print(f"REV {sequence}")
response = c.talk(f"REV {sequence}")
print(response)

print("* Testing GENE...")
for g in genes:
    print(f"GENE {g}")
    response = c.talk(f"GENE {g}")
    print(response)



