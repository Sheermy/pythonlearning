import random

a = random.randint(1, 100)
proby = 0

while True:

    proby += 1

    try:
        b = int(input("Zgadnij liczbę od 1 do 100: "))
    except ValueError:
        print("Niepoprawny znak")
        continue

    if b < a:
        print("Za mało!")
    elif b > a:
        print("Za dużo!")
    else:
        print("Udało ci się zgadnąć w ", proby, " próbach!")

        while True:
            kontynuuj = input("Grasz dalej? (tak / nie): ".lower())
            if kontynuuj == "tak":
                break
            elif kontynuuj == "nie":
                break
            else:
                print("Niepoprawna odpowiedź")

        if kontynuuj == "tak":
            a = random.randint(1, 100)
            proby = 0
            continue
        elif kontynuuj == "nie":
            print("Dzięki za grę!")
            exit()
    
    