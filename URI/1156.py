S = 0
cont = 0
for i in range(1,40):
    if i % 2 != 0:
        S += i/(2**cont)
        cont += 1

print("%.2f" % S)
