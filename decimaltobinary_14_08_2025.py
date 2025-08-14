number = 5374332

binary = []

x = 0

while True:
    inc = 2**x
    if number >= inc:
        x += 1
    else:
        break

y = x
new_number = number

for i in range(x+1):
    if new_number - 2**y >= 0:
        binary.append(1)
        new_number -= 2**y
        y -= 1
    else:
        binary.append(0)
        y -= 1

if binary[0] == 0 and len(binary) > 1:
    binary.pop(0)

print(binary)
