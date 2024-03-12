from pathlib import Path
FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")
total_bases = 0
for line in lines[1:]:
    total_bases += len(line)
print(total_bases)