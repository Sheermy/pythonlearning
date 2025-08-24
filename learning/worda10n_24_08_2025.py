input = "siema to ja guadelupe"

words =  input.split()
output_list = []

for w in words:
    w_list = list(w)
    if len(w_list) > 3:
        w = f"{w_list[0]}{len(w_list)-2}{w_list[-1]}"
        output_list.append(w)
    else:
        output_list.append(w)

output = " ".join(output_list)

print(output)