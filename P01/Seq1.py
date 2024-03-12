class Seq:
    BASES = ['A', 'C', 'T', 'G']

    def __init__(self, strbases = None):
        self.strbases = strbases
        if self.strbases is None or len(strbases) == 0:
            self.strbases = "NULL"
            print("NULL sequence created")
        elif self.seq_valid():
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INCORRECT Sequence detected")

    def __str__(self):
        return self.strbases

    def seq_valid(self):
        for l in self.strbases:
            if l not in ["A", "G", "T", "C"]:
                # print("Error found: ", l)
                return False
        return True

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return self.strbases.count(base)

    def count(self):
        bases_appearances = {}
        for base in Seq.BASES:
            bases_appearances[base] = self.count_base(base)
        return bases_appearances

    #def count(self):
        #base_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        #for base in self.strbases:
            #base_count[base] += 1
        #return base_count

    def reverse(self):
        if self.strbases == "ERROR":
            return "ERROR"
        elif self.strbases == "NULL":
            return "NULL"
        else:
            new_seq = ""
            for c in range(len(self.strbases)):
                new_seq = self.strbases[c] + new_seq
            return new_seq

    def complement(self):
        complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement = ""
        for base in self.strbases:
            complement += complement_bases.get(base, base)
        return complement

    def seq_read_fasta(self, filename):
        from pathlib import Path
        file_content = Path(filename).read_text()
        lines = file_content.splitlines()
        body = lines[1:]
        dna_sequence = ""
        for line in body:
            dna_sequence += line
        return dna_sequence

    def max_base(self):
        bases_dict = {}
        for b in Seq.BASES:
            bases_dict[b] = self.count_base(b)
        most_freq_base = max(bases_dict, key=bases_dict.get)
        return most_freq_base


    def print_seqs(self, seq_list):
        for i in range(len(seq_list)):
            print(f'Sequence {i + 1}: (Length: {seq_list[i].len()}) {seq_list[i]}')

