tekst = "witam tu kutas serdecznie"

words = tekst.split()

letters_count = 0
longest_word = []

for slowo in words:
    letters = list(slowo)
    word = str(slowo)
    counter_helper = 0
    for i in letters:
        counter_helper += 1
    if counter_helper > letters_count:
        longest_word = []
        longest_word.append(word)
        letters_count = counter_helper
    elif counter_helper == letters_count:
        longest_word.append(word)

print(longest_word)