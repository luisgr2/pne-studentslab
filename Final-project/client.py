import http.client
import json
from http import HTTPStatus

SERVER = 'localhost'
PORT = 8080

connection = http.client.HTTPConnection(SERVER, port=PORT)

# chromosomeLength
try:
    connection.request("GET", "/chromosomeLength?species=mouse&chromo=18&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    data = json.loads(data_str)
    print(data)
    chromosome = data['chromosome']
    length = data['length']
    print(chromosome, length)

# geneSeq
try:
    connection.request("GET", "/geneSeq?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode("utf-8")
    data = json.loads(data_str)
    gene = data['gene']
    bases = data['bases']
    print(gene, bases)

try:
    connection.request("GET", "/geneSeq?gene=TEST&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status != HTTPStatus.OK:
    data_str = response.read().decode()
    print(data_str)