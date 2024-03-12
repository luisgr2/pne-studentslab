import os
from Seq0 import *
FOLDER = "sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN"]
BASES = ["A", "C", "T", "G"]

for gene in GENES:
    filename = os.path.join("..", "sequences", gene + ".txt")
    dna_sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}:")
    for base in BASES:
        print(f"\t{base}: {seq_count_bases(dna_sequence, base)}")
