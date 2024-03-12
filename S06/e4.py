from Seq import Seq
import termcolor


def print_seqs(seq_list, color):
    for i in range(len(seq_list)):
        termcolor.cprint(f'Sequence {i}: (Length: {seq_list[i].len()}) {str(seq_list[i])} ', color)


def generate_seqs(pattern, number):
    sequences = []
    for i in range(1, number + 1):
        s = Seq(pattern * i)
        sequences.append(s)
    return sequences


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
