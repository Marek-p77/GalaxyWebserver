####### Moduly #######  Webserver APP made by Marek_p

import http.server   # Import modulu pro http server
import socketserver  # Import modulu pro socket server
import PySimpleGUI as sg # Import staženého modulu pro GUI

####### Úvod #######

print("-----------------------------")
print("| App Name: GalaxyWebserver |")
print("| Version: 1.3              |")
print("| Author: Marek_p           |")
print("-----------------------------")
print("[System] Spouštím GUI...")

####### Menu (GUI) #######

layout = [  [sg.Text("Hostname:", text_color='white', background_color='#000')], # Druhý řádek v GUI
            [sg.Input(background_color='#4E6578')], # Textové pole pro první hodnotu (v našem případě uživatelské jméno) (třetí řádek)
            [sg.Text("Port:", text_color='white', background_color='#000')], # Čtvrtý řádek
            [sg.Input(background_color='#4E6578')], # Textové pole pro druhou hodnotu (v našem případě heslo) (pátý řádek)
            [sg.Text(" ", text_color='white', background_color='#000')], # Mezera mezi textovým polem a tlačítkem (prázdný text na šestém řádku)
            [sg.Button('Spustit Webserver', button_color='#08a4ff')] ] # Tlačítko pro potvrzení / ukončení programu

window = sg.Window('GalaxyWebserver', layout, background_color='#000') # Nadpis GUI + Barva pozadí
event, values = window.read() # Otevření GUI
window.close() # Zavření GUI

####### Webserver #######

print("[System] Spouštím Webserver...") # Zpráva po přijetí dat z GUI

PORT = int(values[1]) # Určení portu z GUI
HOST = str(values[0]) # Určení hostname z GUI
Handler = http.server.SimpleHTTPRequestHandler # Definování handleru

with socketserver.TCPServer((HOST, PORT), Handler) as httpd: # Použití handleru a samotného http serveru
    print("[System] Webserver úspěšně spuštěn na adrese", HOST + " a na portě", PORT) # Zpráva po spuštění
    httpd.serve_forever() # Dlouhodobé spuštení webserveru

