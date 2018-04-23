import OpenSSL
import ssl, socket
import statsd

urls = [for line in open("urls.txt").readlines()]
   
for url in urls:
    cert=ssl.get_server_certificate(('www.google.com', 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    x509.get_notAfter()

