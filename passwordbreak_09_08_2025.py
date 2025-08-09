import string
import itertools
import time

zestaw = string.ascii_letters + string.digits + string.punctuation
lista_zestawu = list(zestaw)
haslo = "abc1"
dlugosc = 1
attempts = 0
attempt = ""
start = time.time()

while True:
    kombinacje = itertools.product(lista_zestawu, repeat=dlugosc)
    for i in kombinacje:
        attempt = "".join(i)
        print(attempt)
        attempts += 1
        if attempt == haslo:
            print("Próby: ", attempts)
            break
    dlugosc += 1
    if attempt == haslo:
        end = time.time()
        length = end - start
        print("It took", length, "seconds!")
        break


