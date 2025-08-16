file = open("test.txt", "r")

line_list = file.readlines()
new_line_list = []

words_cnt = 0
lines_cnt = 0
characters_cnt = 0

for l in line_list:
    if not l.isspace():
        new_line_list.append(l)
        new_l = l.replace("\n", "")

file_new = open("test2.txt", "w")    

for l in new_line_list:
    file_new.write(l)
file_new.close()

file_new = open("test2.txt", "r")

line_list = file_new.readlines()

print(line_list)

for l in line_list:
    lines_cnt += 1
    words = l.split()
    for w in words:
        words_cnt += 1
        characters = list(w)
        for c in characters:
            characters_cnt += 1

print("Linie: ", lines_cnt)
print("Słowa: ", words_cnt)
print("Znaki: ", characters_cnt)