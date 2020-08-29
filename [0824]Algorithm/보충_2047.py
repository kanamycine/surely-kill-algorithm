str_h = input()
resultlist = []
for i in range(len(str_h)):
    if ord(str_h[i]) < 96:
        resultlist.append(str_h[i])
    if ord(str_h[i]) > 96:
        resultlist.append(chr(ord(str_h[i]) - 32))
for j in range(len(resultlist)):
    print(resultlist[j], end='')