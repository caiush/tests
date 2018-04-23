import socket, ssl
import sys
import dateutil.parser
import dateutil.tz
import datetime

url = sys.argv[1]

def _cert_detals(url):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(s, server_hostname=url)
    ssl_sock.connect((url, 443))
    cert = ssl_sock.getpeercert()
    datestr = cert['notAfter']
    expires_on = dateutil.parser.parse(datestr)
    now = datetime.datetime.now(dateutil.tz.tzutc())
    return (expires_on - now).total_seconds()

def _load_urls():
    with open("urls.txt") as f:
        urls = [line.split() for line in f]
    return urls

for url in _load_urls():    
    print(url,_cert_detals(url[1]))


    
