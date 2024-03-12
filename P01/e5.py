from Seq1 import Seq
print("-----| Practice 1, Exercise 5 |------")

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for i, s in enumerate(seq_list):
    print(f"Sequence {i }: (Length: {s.len()}) {s}")
    for b in ['A', 'C', 'T', 'G']:
        print(f"\t{b}: {s.count_base(b)}", end='')
    print()
