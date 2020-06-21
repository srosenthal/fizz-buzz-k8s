from http.server import HTTPServer, BaseHTTPRequestHandler
import platform
import urllib.request


fizz_url = "http://fizzer:7080"
buzz_url = "http://buzzer:9080"


def http_get(url):
    with urllib.request.urlopen(url) as response:
        b = response.read()
        return b.decode("utf-8")


def do_fizz_buzz():
    lines = []
    for n in range(1, 50):
        if n % 5 == 0 and n % 3 == 0:
            fizz = http_get(fizz_url)
            buzz = http_get(buzz_url)
            lines.append(f"{fizz} {buzz}")
        elif n % 3 == 0:
            fizz = http_get(fizz_url)
            lines.append(f"{fizz}")
        elif n % 5 == 0:
            buzz = http_get(buzz_url)
            lines.append(f"{buzz}")
        else:
            lines.append(f"<{n}, from {platform.node()}>")
    return "\n".join(lines)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        try:
            msg = do_fizz_buzz()
        except BaseException as e:
            msg = str(e)
        self.wfile.write(str.encode(msg))


httpd = HTTPServer(("0.0.0.0", 8080), SimpleHTTPRequestHandler)
print("Starting the LOOPER...")
httpd.serve_forever()