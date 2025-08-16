txt = "aaabbbccc11234"
txt_list = list(txt)
txt_list.sort()
chars = {

}

for i in txt_list:
    if i in chars:
        chars[i] += 1
    else:
        chars.update({i: 1})


for keys,values in chars.items():
    print(keys,":", values)