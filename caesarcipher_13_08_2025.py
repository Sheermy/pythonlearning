inp = "zx12309!-0=$%,./"
outp = []
step = 4

for i in inp:
    cipher = ord(i)
    cipher = cipher+step
    cipher = chr(cipher)
    outp.append(cipher)

outp = "".join(outp)
print(outp)