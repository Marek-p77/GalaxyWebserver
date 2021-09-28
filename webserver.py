from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html' # Spouštěcí soubor
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = '[Error] Soubor nenalezen!' # Error zpráva
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8')) # Encoding


httpd = HTTPServer(('localhost', 8080), Serv) # Hostname + Port
httpd.serve_forever()
