from Seq0 import *
FOLDER = "sequences/"
FILENAME = "U5.txt"
dna_sequence = seq_read_fasta(FOLDER + FILENAME)
print("DNA file:", FILENAME)
print("The first 20 bases are:\n", dna_sequence[:20])

