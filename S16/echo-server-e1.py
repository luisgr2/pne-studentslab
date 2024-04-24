import http.server
import socketserver
import termcolor
import os
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j


def read_html_file(filename):
    file_path = os.path.join(HTML_FOLDER, filename)
    contents = Path(file_path).read_text()
    contents = j.Template(contents)
    return contents


PORT = 8080
HTML_FOLDER = "html"

socketserver.TCPServer.allow_reuse_address = True


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        print(f"Path: {path}")
        arguments = parse_qs(url_path.query)
        print(f"Arguments: {arguments}")
        if path == "/":
            file_path = os.path.join(HTML_FOLDER, "form-e1.html")
            contents = Path(file_path).read_text()
            self.send_response(200)
        elif path == "/echo":
            try:
                msg_param = arguments['msg'][0]
                print(msg_param)
                contents = read_html_file("result-e1.html").render(context={"todisplay": msg_param})
                self.send_response(200)
            except (KeyError, IndexError):
                file_path = os.path.join(HTML_FOLDER, "error")
                contents = Path(file_path).read_text()
                self.send_response(404)
        else:
            contents = Path(f"{HTML_FOLDER}/error.html").read_text()
            self.send_response(404)

        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)


with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT...", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()