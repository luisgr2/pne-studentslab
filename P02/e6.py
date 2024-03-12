from Seq1 import Seq
from Client0 import Client
import os

gene = "FRAT1"
print(f"-----| Practice 2, Exercise 6 |------")
number_fragments = 10
number_bases = 10

IP_1 = ""
PORT_1 =
c = Client(IP_1, PORT_1)
print(c)

IP_2 = ""
PORT_2 = 8082
l = Client(IP_2, PORT_2)
print(l)

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
        if i % 2 == 0:
            response = l.talk(gene_sequence)
            print(f"From server: {response}")
        else:
            response = c.talk(gene_sequence)
            print(f"From server: {response}")
except FileNotFoundError:
    print(f"Error: file {filename} not found!")
