import collections

tekst = "kutas"
vowels = "aeiouyAEIOUY"
cnt = (collections.Counter(i for i in tekst if i in vowels))
ammount = sum(cnt.values())

print(ammount)