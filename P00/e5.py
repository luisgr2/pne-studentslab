import os
from Seq0 import *
FOLDER = "sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN"]

for gene in GENES:
    filename = os.path.join("..", "sequences", gene + ".txt")
    dna_sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}: {seq_count(dna_sequence)}")