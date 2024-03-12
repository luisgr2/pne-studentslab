class Seq:
    BASES = ['A', 'C', 'T', 'G']

    def __init__(self, strbases):
        self.strbases = strbases
        if self.seq_valid():
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    def seq_valid(self):
        ok = True
        for l in self.strbases:
            if l not in ["A", "G", "T", "C"]:
                ok = False
                break
        return ok


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    first_line = file_contents.find("\n")
    sequence = file_contents[first_line:]
    print("The first 20 bases are:", sequence[0:21])


def seq_len(seq):
    n = ["A", "C", "G", "T"]
    total = 0
    for i in seq:
        if i in n:
            total += 1
    return total


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    bases = {"A": 0, "C": 0, "G": 0}
    for base in seq:
        if base in bases:
            bases[base] += 1
    return bases


def seq_reverse(seq, n=None):
    if n is None:
        n = len(seq)
    new_seq = ""
    for c in range(n):
        new_seq = seq[c] + new_seq
    return new_seq


def seq_complement(seq):
    complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ""
    for base in seq:
        complement += complement_bases.get(base, base)
    return complement
