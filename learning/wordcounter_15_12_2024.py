while True:
    text = input("Wpisz tekst: ")

    if text.lower() == "koniec":
        print("Program zakończony.")
        break

    slowa = text.split()
    liczba_slow = len(slowa)

    liczba_znakow = len(text.replace(" ", ""))

    print(f"Liczba słów: {liczba_slow}")
    print(f"Liczba znaków: {liczba_znakow}")
