
pytania = [
        {"pytanie": "Stolicą Francji jest?", "poprawna": "Paryż"},
        {"pytanie": "2 + 2 to?", "poprawna": "4"},
        {"pytanie": "Jaki jest najdłuższy rzeka świata?", "poprawna": "Amazonka"},
    ]

punkty = 0

def rozpocznij_quiz(pytania, punkty):
    print("Witaj w quizie! Odpowiedz na poniższe pytania.\n")

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
        


while True:
    akcja = input("Wybierz akcję:\n1. Rozwiąż quiz\n2. Dodaj pytanie\n3. Zobacz wyniki\n")

    if akcja == "1":
        rozpocznij_quiz(pytania, punkty)
    elif akcja == "2":
        pytanie = input("Wpisz pytanie: ")
        odpowiedz = input("Wpisz poprawną odpowiedź: ").lower()
        nowe_pytanie = {"pytanie": pytanie, "poprawna": odpowiedz}
        pytania.append(nowe_pytanie)
    else:
        continue