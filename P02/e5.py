from Seq1 import Seq
from Client0 import Client
import os

gene = "FRAT1"
print(f"-----| Practice 2, Exercise 5 |------")
number_fragments =5
number_bases = 10

IP = "192.168.0.30"
PORT = 8081
c = Client(IP, PORT)
print(c)
filename = os.path.join("sequences", gene + ".txt")
try:
    s = Seq()
    s.read_fasta(filename)
    print(f"Gene {gene}: {s}")
    gene_sequence = str(s)
    for i in range(number_fragments):
        start_index = i * number_bases
        end_index = start_index + number_bases
        fragment = gene_sequence[start_index:end_index]
        print(f"Fragment {i + 1}: {fragment}")

    msg = str(s)
    print(f"To server: {msg}")
    response = c.talk(msg)
    print(f"From server: {response}")
except FileNotFoundError:
    print(f"Error: file {filename} not found!")
