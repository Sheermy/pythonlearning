a = int(input("Od: "))
b = int(input("Do: "))

prime_numbers = []

for i in range(a, b+1):
    dividers = 0
    for k in range(i):
        if i % (k+1) == 0:
            dividers += 1
    if dividers == 2:
        prime_numbers.append(i)

print(prime_numbers)