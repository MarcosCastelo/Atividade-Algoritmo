n = int(input())
lista = []
for i in range(1000):
    for j in range(n):
        lista.append(j)
    print("N[%d] = %d" % (i, lista[i]))
