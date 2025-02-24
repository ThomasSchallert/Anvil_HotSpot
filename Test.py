import alvikController as ac
import requests

controller = ac.AlvikController("iPhone von Jannik", "Lajani17-LTE")

if controller.connect_to_wifi():
    print("Roboter verbunden. IP-Adresse:", controller.ip_address)

    # Ziel-URL
    url = f"http://{controller.ip_address}/command?dir=up"

    try:
        # GET-Anfrage senden
        response = requests.get(url)
        
        # Status und Antwort ausgeben
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        
        # Fehlerbehandlung
        if response.status_code == 200:
            print("Befehl erfolgreich gesendet.")
        else:
            print("Fehler bei der Anfrage:", response.status_code)
    except requests.RequestException as e:
        print("Anfrage fehlgeschlagen:", e)
else:
    print("Wi-Fi-Verbindung fehlgeschlagen.")
