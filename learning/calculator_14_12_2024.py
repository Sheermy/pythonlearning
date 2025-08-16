import math

print("Dostępne operacje:\n\n'+' - dodawanie\n'-' - odejmowanie\n'*' - mnożenie\n'/' - dzielenie\n'sqrt' - pierwiastkowanie\n'^' - potęgowanie\n'sin' - funkcja sinus\n'cos' - funkcja cosinus\n ")

while True:


    try:
        a = float(input("Podaj pierwszą liczbę:"))
        b = float(input("Podaj drugą liczbę:"))
    except ValueError:
        print("Błąd")
        continue
    
    
    operacja = input("Jaka operacja? (+ - * / sqrt sin cos ^): ")


    if operacja == "*":
        wynik = a * b
    elif operacja == "+":
        wynik = a + b
    elif operacja == "sin":
        sinus = math.sin(math.radians(a))
        wynik = float(sinus)
    elif operacja == "cos":
        cosinus = math.cos(math.radians(a))
        wynik = float(cosinus)
    elif operacja == "^":
        wynik = a ** b
    elif operacja == "sqrt":
        if a < 0:
            print("Błąd: pierwiastek liczby ujemnej nie mieści się w zbiorze liczb rzeczywistych")
            continue
        pierwiastek = math.sqrt(a)
        wynik = float(pierwiastek)
    elif operacja == "-":
        wynik = a - b
    elif operacja == "/":
        if  b == 0:
            print("Błąd: nie można dzielić przez 0")
            continue
        wynik = a / b
    else:
        print("Niepoprawna komenda")
        continue

    print("Wynik to ", round(wynik, 5))

