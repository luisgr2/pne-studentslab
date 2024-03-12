from pathlib import Path
FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
first_line = file_contents.split('\n')
print(first_line[0])
