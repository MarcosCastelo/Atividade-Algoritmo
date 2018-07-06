def reverse(lista):
    nova_lista = []
    for item in lista:
        novo_item = ""
        for i in range(len(item)-1,-1,-1):
            novo_item += item[i]
        nova_lista.append(novo_item)

    return nova_lista

t = ["Maçã", "Arara", "Uva"]
print(reverse(t))
