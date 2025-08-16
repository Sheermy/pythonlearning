h = 12
stars = 0

for i in range(h):
    stars += 1
    print("* "*stars)

stars = 0

for i in range(h):
    stars += 1
    print(" "*(h-stars)+" *"*stars)
