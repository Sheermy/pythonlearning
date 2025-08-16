import random

while True:
    try:
        walls = int(input("Ilościenna kostka?: "))
        rolls = int(input("Ile rzutów?: "))
        if walls < 4:
            print("Kostka nie może mieć mniej ścian niż 4")
        elif rolls < 1:
            print("Niepoprawna ilość rzutów")
    except ValueError:
        print("Niepoprawna wartość")
        continue
    else:
        print("Wyniki: \n")
        while rolls > 0:
            wynik = random.randrange(1, walls+1)
            print(wynik)
            rolls -= 1
        wybor = input("Chcesz rzucić kostką? (tak/nie): ").lower()
        if wybor == "nie":
            print("Dziękujemy za grę!")
            break
