import random
aniversarios = [[]]
soma = 0
ocorrencias = 1

def has_duplicate(lista):
    new_lista = []
    for item in lista:
        if item not in new_lista:
            new_lista.append(item)
    if new_lista == lista:
        return False
    else:
        return True
for i in range(100):
    aniversario = []
    for j in range(1,24):
        aniversario.append(random.randint(1,365))

    aniversarios.append(aniversario)

    if has_duplicate(aniversarios[i]):
        ocorrencias += 1
print(ocorrencias,"%")
