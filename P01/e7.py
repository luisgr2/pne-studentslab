from Seq1 import Seq
print("-----| Practice 1, Exercise 7 |------")
seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for i, s in enumerate(seq_list):
    print(f"Sequence {i }: (Length: {s.len()}) {s}")
    print(f"\tBases: {s.count()}")
    print(f"\tRev: {s.reverse()}")