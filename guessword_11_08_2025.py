import random

words = ["chuj", "cwel", "kutas", "szmata", "dziwka"]

random_word = random.choice(words)

while True:
    guess = str(input("Zgadnij słowo: "))
    if guess == random_word:
        print("Zgadłeś! Słowo to: ", random_word)
        break
    else:
        print("Pojebany?")