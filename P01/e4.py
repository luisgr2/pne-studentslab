from Seq1 import Seq
print("-----| Practice 1, Exercise 4 |------")

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for i, s in enumerate(seq_list):
    print(f"Sequence {i + 1}: Length: {s.len()}) {s}")