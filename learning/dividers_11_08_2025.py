
while True:
    number = int(input("Podaj liczbę: "))
    dividers = []

    for i in range (number):
        x = i+1
        if number % x == 0:
            dividers.append(x)

    print(dividers)