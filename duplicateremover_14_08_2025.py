list = [1, 3 , 2, "a", "a", 2, 3, "a", "b", "c", "c", "b"]
help_list = []

for i in list:
    if i in help_list:
        continue
    else:
        help_list.append(i)

list = help_list
print(list)