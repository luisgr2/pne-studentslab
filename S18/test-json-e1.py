import json
import termcolor
from pathlib import Path

json_string = Path("people-e1.json").read_text()
persons = json.loads(json_string)["people"]
print(f"Total people on the database {len(persons)}")
for p in persons:

    termcolor.cprint("Name:", 'green',end="")
    print(p['Firstname'], p['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(p['age'])
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(p['phoneNumber']))

    for i, num in enumerate(p['phoneNumber']):
        termcolor.cprint("  Phone {}:".format(i), 'blue')
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])