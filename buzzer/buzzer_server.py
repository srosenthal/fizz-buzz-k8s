from http.server import HTTPServer, BaseHTTPRequestHandler
import platform


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg = f"<BUZZ, from {platform.node()}>"
        self.wfile.write(str.encode(msg))


httpd = HTTPServer(("0.0.0.0", 9080), SimpleHTTPRequestHandler)
print("Starting the BUZZER...")
httpd.serve_forever()