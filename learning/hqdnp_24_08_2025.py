items = {
    "H" : 0,
    "Q" : 0,
    "D" : 0,
    "N" : 0,
    "P" : 0
}

quota = 167

def Exchanger(n):
    while n - 50 >= 0:
        n -= 50 
        items["H"] = items.get("H") + 1
    while n - 25 >= 0:
        n -= 25
        items["Q"] = items.get("Q") + 1
    while n - 10 >= 0:
        n -= 10 
        items["D"] = items.get("D") + 1
    while n - 5 >= 0:
        n -= 5
        items["N"] = items.get("N") + 1
    while n - 1 >= 0:
        n -= 1
        items["P"] = items.get("P") + 1

Exchanger(quota)

print(items)
