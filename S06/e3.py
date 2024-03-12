from Seq import Seq


def generate_seqs(pattern, number):
    sequences = []
    for i in range(1, number + 1):
        s = Seq(pattern * i)
        sequences.append(s)
    return sequences


def print_seqs(seq_list):
    for i, s in enumerate(seq_list):
        print(f"Sequence {i}: (Length: {s.len()}) {s}")


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
