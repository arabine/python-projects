# http_server.py
import shutil
import socketserver
import sys
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from io import BytesIO


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)

def run_http_server(port):
    with socketserver.TCPServer(("", port), RequestHandler) as httpd:
        try:
            httpd.serve_forever()
        finally:
            httpd.server_close()


print("Running HTTP server on port 3000")
run_http_server(3000) 
