from Seq import Seq


#def print_seqs(seq_list):
#   for i in seq_list:
#      print(f"Sequence {seq_list.index(i)}: (Length: {i.len()} {i}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for i, s in enumerate(seq_list):
    print(f"Sequence {i}: (Length: {s.len()} {s}")

