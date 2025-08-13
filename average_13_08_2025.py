liczby = []

while True:
    suma = 0
    liczba = float(input("Podaj liczbę: "))
    liczby.append(liczba)
    for i in liczby:
        suma += i
    average = suma/len(liczby)
    print(average)