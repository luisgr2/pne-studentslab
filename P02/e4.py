from Seq1 import Seq
from Client0 import Client
import os

genes = ["U5", "FRAT1", "ADA"]

print(f"-----| Practice 2, Exercise 4 |------")

IP = "192.168.0.30"
PORT = 8081
c = Client(IP, PORT)
print(c)

for g in genes:
    filename = os.path.join("sequences", g + ".txt")
    try:
        s = Seq()
        s.read_fasta(filename)

        msg = f"Sending {g} Gene to the server:"
        print(f"To server: {msg}")
        response = c.talk(msg)
        print(f"From server: {response}")

        msg = str(s)
        print(f"To server: {msg}")
        response = c.talk(msg)
        print(f"From server: {response}")
    except FileNotFoundError:
        print("File not found")






