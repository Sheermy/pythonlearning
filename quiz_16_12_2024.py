
pytania = [
        {"pytanie": "Stolicą Francji jest?", "poprawna": "Paryż"},
        {"pytanie": "2 + 2 to?", "poprawna": "4"},
        {"pytanie": "Jaki jest najdłuższy rzeka świata?", "poprawna": "Amazonka"},
    ]

punkty = 0

nick = ""

def wczytaj_wyniki():
    nazwa_pliku = "wyniki_quizu.txt"

    try:
        with open(nazwa_pliku, "r") as plik:
            zawartosc = plik.readlines()
            if not zawartosc:
                print("Brak zapisanych wyników.")
            else:
                print("\nZapisane wyniki:")
                for linia in zawartosc:
                    print(linia.strip())
    except FileNotFoundError:
        print("Plik z wynikami nie istnieje. Nie zapisano jeszcze żadnych wyników.")

def rozpocznij_quiz(pytania, punkty, nick):
    print("Witaj w quizie! Odpowiedz na poniższe pytania.\n")
    nick = input("Podaj nick:")

    for indeks, element in enumerate(pytania, start=1):
        print(f"Pytanie {indeks}: {element['pytanie']}")
        
        odpowiedz = input("Twoja odpowiedź: ").strip()

        if odpowiedz.lower() == element["poprawna"].lower():
            print("Poprawna odpowiedź!\n")
            punkty += 1
        else:
            print(f"Błędna odpowiedź. Poprawna odpowiedź to: {element['poprawna']}\n")

    print(f"Twój wynik to: {punkty}/{len(pytania)}")
    print("Dziękujemy za udział w quizie!")

    wynik = f"Użytkownik: {nick}, Wynik: {punkty}/{len(pytania)}\n"
    
    with open("wyniki_quizu.txt", "a") as plik:
        plik.write(wynik)
        


while True:
    akcja = input("Wybierz akcję:\n1. Rozwiąż quiz\n2. Dodaj pytanie\n3. Zobacz wyniki\n")

    if akcja == "1":
        rozpocznij_quiz(pytania, punkty, nick)
    elif akcja == "2":
        pytanie = input("Wpisz pytanie: ")
        odpowiedz = input("Wpisz poprawną odpowiedź: ").lower()
        nowe_pytanie = {"pytanie": pytanie, "poprawna": odpowiedz}
        pytania.append(nowe_pytanie)
    elif akcja == "3":
        wczytaj_wyniki()
    else:
        continue