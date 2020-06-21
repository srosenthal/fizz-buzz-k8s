from http.server import HTTPServer, BaseHTTPRequestHandler
import platform


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg = f"<FIZZ, from {platform.node()}>"
        self.wfile.write(str.encode(msg))


httpd = HTTPServer(("0.0.0.0", 7080), SimpleHTTPRequestHandler)
print("Starting the FIZZER...")
httpd.serve_forever()