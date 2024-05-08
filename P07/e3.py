import http.client
import json
from http import HTTPStatus

GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

GENE = "MIR633"
SERVER = 'rest.ensembl.org'
RESOURCE = f'/sequence/id/{GENES[GENE]}'
PARAMS = '?content-type=application/json'
URL = RESOURCE + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", URL)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    data = json.loads(data_str)
    print(data)
    print(f"Gene: {GENE}")
    print(f"Description: {data['desc']}")
    print(f"Bases: {data['seq']}")
