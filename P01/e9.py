from Seq1 import Seq
print("-----| Practice 1, Exercise 9 |------")
s = Seq()
filename = "sequences/U5.txt"
try:
    s.seq_read_fasta(filename)
    print(f"Sequence: (Length: {s.len()}) {s} \n Bases: {s.count()} \n Rev: {s.reverse()} \n Comp: {s.complement()}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")