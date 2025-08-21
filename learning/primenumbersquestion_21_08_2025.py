file = open("learning/liczby.txt", "r")
numbers = []

for i in file.readlines():
    n = i.replace("\n", "")
    numbers.append(n)

prime_numbers = []

for n in numbers:
    n = int(n)
    divs = 0
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            divs += 1
    if divs == 0:
        prime_numbers.append(n)

palindroms = []

for n in numbers:
    if str(n) == str(n)[::-1]:
        palindroms.append(n)

prime_numbers.sort()
high_prime = str(prime_numbers[-1])

if high_prime in numbers:
    row = numbers.index(high_prime) + 1

wyniks = open("learning/wyniki21082025_1.txt", "w")

wyniks.write(f"Liczb pierwszych: {len(prime_numbers)}\n")
wyniks.write(f"Najwieksza liczba pierwsza: {prime_numbers[-1]} (wiersz nr {row})\n")
wyniks.write(f"Palindromy: {palindroms}")