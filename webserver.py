import http.server   # Import modulu pro http server
import socketserver  # Import modulu pro socket server

PORT = 8080 # Port webserveru
HOST = "localhost" # Hostname webserveru
Handler = http.server.SimpleHTTPRequestHandler # Definování handleru

with socketserver.TCPServer((HOST, PORT), Handler) as httpd: # Použití handleru a samotného http serveru
    print("[System] Webserver spuštěn na adrese", HOST + " a portu", PORT) # Zpráva v konzoli po spuštění
    httpd.serve_forever() # Dlouhodobé spuštení webserveru
