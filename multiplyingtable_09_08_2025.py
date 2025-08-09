
def mnozenie(x, y):
    a = 1
    for b in range(x, y+1):
        wyniki = []
        for i in range(x, y+1):
            wynik = a * i
            wyniki.append(wynik)
        print(wyniki)
        a += 1

mnozenie(1, 10)