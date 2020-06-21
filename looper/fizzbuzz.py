import urllib.request

def http_get(url):
    with urllib.request.urlopen(url) as response:
        b = response.read()
        return b.decode('utf-8')

for n in range(0, 50):
    if n % 5 == 0 and n % 3 == 0:
        fizz = http_get('http://localhost:7000')
        buzz = http_get('http://localhost:9000')
        print(f"{fizz} {buzz}")
    elif n % 3 == 0:
        fizz = http_get('http://localhost:7000')
        print(f"{fizz}")
    elif n % 5 == 0:
        buzz = http_get('http://localhost:9000')
        print(f"{buzz}")
    else:
        print(n)