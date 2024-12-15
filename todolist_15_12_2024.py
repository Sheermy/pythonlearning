import os

def dodaj_zadanie(lista):
    zadanie = input("Wpisz treść zadania: ")
    lista.append(zadanie)
    print("Dodano zadanie.")

def wczytaj_liste(nazwa_pliku):
    if not os.path.exists(nazwa_pliku):
        return []
    with open(nazwa_pliku, "r") as plik:
        return [linia.strip() for linia in plik.readlines()]
    
def zapisz_liste(lista, nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        for zadanie in lista:
            plik.write(zadanie + "\n")
    
nazwa_pliku = "lista_zadan.txt"
lista_zadan = wczytaj_liste(nazwa_pliku)

while True:
    print("\nLista rzeczy do zrobienia:")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Wyświetl listę zadań")
    print("4. Zakończ")
    print("5. Posortuj listę zadań")

    wybor = input("Wybierz opcję (1-5): ")
    print("\n")

    if wybor == "1":
        dodaj_zadanie(lista_zadan)
        zapisz_liste(lista_zadan, nazwa_pliku)
    elif wybor == "2":
        if len(lista_zadan) == 0:
            print("Lista jest pusta!")
        else:
            for i, zadanie in enumerate(lista_zadan, start=1):
                print(f"{i}. {zadanie}")

            try:
                numer = int(input("Wpisz numer zadania do usunięcia: "))
                if 1 <= numer <= len(lista_zadan):
                    usuniete = lista_zadan.pop(numer - 1)  
                    print(f"Usunięto zadanie: '{usuniete}'")
                else:
                    print("Niepoprawny numer.")
            except ValueError:
                print("Wprowadź poprawny numer!")
            zapisz_liste(lista_zadan, nazwa_pliku)
    elif wybor == "3":
        if len(lista_zadan) == 0:
            print("Lista jest pusta!")
        else:
            for i, zadanie in enumerate(lista_zadan, start=1):
                print(f"{i}. {zadanie}")

    elif wybor == "4":
        print("Dziękujemy za skorzystanie z programu. Do zobaczenia!")
        exit()
    elif wybor == "5":
        lista_zadan.sort()
        print("Lista została posortowana alfabetycznie.")
        zapisz_liste(lista_zadan, nazwa_pliku)
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")