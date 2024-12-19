from datetime import datetime

import json

kalendarz = {
    "2024-12-25": ["Spotkanie wigilijne", "Kup prezenty"],
    "2024-01-01": ["Noworoczne postanowienia"]
}

def zapisz_do_pliku(kalendarz, nazwa_pliku="kalendarz.json"):
    with open(nazwa_pliku, "w") as plik:
        json.dump(kalendarz, plik)
    print("Zapisano dane do pliku.")

data = input("Podaj datę (YYYY-MM-DD): ")
try:
    data_parsed = datetime.strptime(data, "%Y-%m-%d")
    print("Poprawna data:", data_parsed)
except ValueError:
    print("Niepoprawny format daty!")

def dodaj_wydarzenie(kalendarz, data, wydarzenie):
    zapisz_do_pliku(kalendarz, nazwa_pliku="kalendarz.json")
    if data in kalendarz:
        kalendarz[data].append(wydarzenie)
    else:
        kalendarz[data] = [wydarzenie]
    print(f"Dodano wydarzenie: {wydarzenie} na dzień {data}")

def wyswietl_wydarzenia(kalendarz, data=None):
    wczytaj_z_pliku(nazwa_pliku="kalendarz.json"):
    if data:
        if data in kalendarz:
            print(f"Wydarzenia na {data}: {kalendarz[data]}")
        else:
            print(f"Brak wydarzeń na {data}.")
    else:
        print("Wszystkie wydarzenia:")
        for data, wydarzenia in kalendarz.items():
            print(f"{data}: {', '.join(wydarzenia)}")

def wczytaj_z_pliku(nazwa_pliku="kalendarz.json"):
    try:
        with open(nazwa_pliku, "r") as plik:
            return json.load(plik)
    except FileNotFoundError:
        print("Brak zapisanych wydarzeń. Tworzę nowy kalendarz.")
        return {}
        