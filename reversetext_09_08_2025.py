while True:
    tekst = str(input("Podaj tekst:"))
    lista = list(tekst)
    lista.reverse()
    reversed = "".join(lista)

    print(reversed)