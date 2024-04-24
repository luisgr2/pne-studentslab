import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
def webpage(request):
    page = request.split('/')[1]

    if page == "info" and len(request.split('/')) == 3:
        filename = f"html/{request[1:]}.html"
    elif page == "":
        filename = "html/index.html"
    else:
        filename = "html/error.html"
    return filename


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        page = self.path
        filename = webpage(page)
        try:
            f = open(filename, "r")
            contents = f.read() + "\n"
        except FileNotFoundError:
            filename = "html/error.html"
            f = open(filename, "r")
            contents = f.read() + "\n"
            print("The file does not exist.")

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(contents.encode())
        return


# -- Set the new handler
Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()