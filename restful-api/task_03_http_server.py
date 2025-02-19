from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.headers('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.headers('Content-type', 'application.json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    server_adress = ('', 8000)
    httpd = server_class(server_adress, handler_class)
    print(f"Server running on port {8000}...")
    httpd.serve_forever


if __name__ == "__main__":
    run()
