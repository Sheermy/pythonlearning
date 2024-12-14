import random
import string

def password_generation(dlugosc, zestaw):
    haslo = ''.join(random.choices(zestaw, k=dlugosc))
    print(haslo)
    

while True:
    try:
        dlugosc = int(input("Podaj długość hasła: "))
        if dlugosc <= 0:
            print("Długość hasła musi być większa niż 0.")
            continue
        czy_litery = input("Czy hasło ma zawierać litery? (tak/nie): ").lower() == "tak"
        czy_cyfry = input("Czy hasło ma zawierać cyfry? (tak/nie): ").lower() == "tak"
        czy_znaki = input("Czy hasło ma zawierać znaki specjalne? (tak/nie): ").lower() == "tak"
        ilosc = int(input("Podaj ilośc haseł: "))
        if ilosc < 0:
            print("Ilość nie może być ujemna")
            continue

    except ValueError:
        print("Zły format odpowiedzi")
        continue

    zestaw = ""
    if czy_litery:
        zestaw += string.ascii_letters
    if czy_cyfry:
        zestaw += string.digits
    if czy_znaki:
        zestaw += string.punctuation

    if not zestaw:
        print("Nie wybrano żadnych znaków! Ustawiam domyślnie litery.")
        zestaw = string.ascii_letters

    print("\nWygenerowane hasła: \n")
    for _ in range(ilosc):
        password_generation(dlugosc, zestaw)
    print("\n")

    kontynuuj = input("\nCzy chcesz wygenerować kolejne hasła? (tak/nie): \n").lower()
    if kontynuuj != "tak":
        break