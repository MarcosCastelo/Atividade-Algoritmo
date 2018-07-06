lista = []
pos = int(input())
oper = input()

for i in range(12):
    aux = []
    for j in range(12):
        n = float(input())
        aux.append(n)
    lista.append(aux)

if oper == "S":
    soma = 0
    for i in range(len(lista)):
        soma += lista[i][pos]
    print("%.1f" % soma)
elif oper == "M":
    soma = 0
    for i in range(len(lista)):
        soma += lista[i][pos]
    media = soma / len(lista[pos])
    print("%.1f" % media)
