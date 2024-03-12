import socket
import os
import termcolor
from seq import Seq

IP = "127.0.0.1"
PORT = 8080
SEQUENCES = ["ACTGACTGAA", "CATAAGCGTAGC", "CTATACGTA", "CCCC", "CAACCAACAC"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    print("SEQ Server configured!")

    while True:
        print(f"Waiting for connections at ({IP}:{PORT})...")
        (client_socket, client_address) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode()

        lines = request.splitlines()
        slices = lines[0].split(' ')
        command = slices[0]
        termcolor.cprint(command, 'green')
        if command == "PING":
            response = "OK!\n"

        elif command == "GET":
            n = int(slices[1])
            bases = SEQUENCES[n]
            s = Seq(bases)
            #filename = os.path.join("sequences", gene + ".txt")
            #s.read_fasta(filename)
            response = str(s)
        elif command == "INFO":
            bases = slices[1]
            s = Seq(bases)
            response = s.info()
        elif command == "COMP":
            bases = slices[1]
            s = Seq(bases)
            response = s.complement()
        elif command == "REV":
            bases = slices[1]
            s = Seq(bases)
            response = s.reverse()
        elif command == "GENE":
            gene = slices[1]
            s = Seq()
            filename = os.path.join("sequences", gene + ".txt")
            s.read_fasta(filename)
            response = str(s)
        #añadiremos mas opciones al servidor de la misma forma


        print(response)
        response_bytes = response.encode()
        client_socket.send(response_bytes)

        client_socket.close()
#except socket.error:
    #print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:
    print("Server stopped by the admin")
    server_socket.close()