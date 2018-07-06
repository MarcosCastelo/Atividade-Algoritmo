def nested_sum(lista):
    soma = 0
    for i in lista:
        soma += sum(i)
    return soma
t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
