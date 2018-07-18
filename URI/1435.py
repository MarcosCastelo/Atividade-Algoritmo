matriz = []

n = int(input())
indice = 1
inicio = 0
fim = n-1
for i in range(n):
    vetor = []
    for j in range(n):
        if j >= inicio and j <= fim:
            vetor.append(indice)
        else:
            vetor.append(indice-1)
    matriz.append(vetor)
    inicio += 1
    fim -= 1
    indice += 1

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end="")
    print()