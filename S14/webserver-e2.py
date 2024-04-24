import http.server
import socketserver
import termcolor
import os

PORT = 8080
document_root = "documents"

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        if self.path == '/' or self.path == '/index.html':
            file_path = os.path.join(document_root, 'index.html')
            self.serve_file(file_path, 'text/html')
        else:
            file_path = os.path.join(document_root, 'error.html')
            self.serve_file(file_path, 'text/html', 404)

    def serve_file(self, file_path, content_type, status=200):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                contents = file.read()
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', len(contents))
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_error(404, "File Not Found")


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()