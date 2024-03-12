from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for g in genes:
    filename = "sequences/"+ g + ".txt"
    s = Seq()
    s.seq_read_fasta(filename)
    print(f"Gene {g}: Most frequent Base: {s.max_base()}")