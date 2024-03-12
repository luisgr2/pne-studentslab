from pathlib import Path
FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")
print(f"Body of the {FILENAME} file:")
for line in lines[1:]:
    print(line)