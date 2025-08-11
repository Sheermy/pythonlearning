number = 463
numberstr = str(number)
digits = list(numberstr)

sum = 0

for i in digits:
    i = int(i)
    sum += i

print(sum)