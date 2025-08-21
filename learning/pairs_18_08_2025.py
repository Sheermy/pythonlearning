file = open("learning/pary", "r")
ints = []


for l in file.readlines():
    l = l.split()
    ints.append(l[0])

for i in ints:
    i = int(i)
    if i > 4 and i % 2 == 0:
        print(i)
        x = 3
        y = i-x
        x_div = 0
        y_div = 0
        for n in range(y):
            if y % (n+1) == 0:
                y_div += 1
            if x % (n+1) == 0:
                x_div += 1
            if y_div == 2 and x_div == 2 and x + y == i:
                print (i, x, y)
                break




