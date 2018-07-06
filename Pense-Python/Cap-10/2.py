def cumsum(lista):
    new_lista = []
    for i in range(len(lista)):
        soma = 0
        for j in range(i+1):
            soma += lista[j]
        new_lista.append(soma)
    return new_lista
t = [2, 3, 4]
print(cumsum(t))
