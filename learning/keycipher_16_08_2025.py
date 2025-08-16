import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

char_list = list(chars)
key = char_list.copy()

random.shuffle(key)

input_text = input("Text: ")
cypher_text = ""

input_text_list = list(input_text)

for c in input_text_list:
    index = char_list.index(c)
    cypher_text += key[index]

print(cypher_text)

input_text = input("Text: ")
decypher_text = ""

input_text_list = list(input_text)

for c in input_text_list:
    index = key.index(c)
    decypher_text += char_list[index]

print(decypher_text)