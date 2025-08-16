tekst = "kayak"

front = list(tekst)
back = list(tekst)
back.reverse()

if front == back:
    print("Palindrom")
else:
    print("Na-ah")