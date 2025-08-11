list_a = [1, 2, 3, 4, 5, 6]
list_b = [1, 3, 5, 7, 9]

list_c = []
list_d = []

for i in list_a:
    if i in list_b:
        list_c.append(i)
    else:
        list_d.append(i)

print("Częśc wspólna: ", list_c)

