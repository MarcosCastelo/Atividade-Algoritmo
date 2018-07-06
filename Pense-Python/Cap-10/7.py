def has_duplicate(lista):
    new_lista = []
    # new_lista = list(set(lista))
    for item in lista:
        if item not in new_lista:
            new_lista.append(item)
    if new_lista == lista:
        return False
    else:
        return True


t = [1, 2, 3, 3, 4]
print(has_duplicate(t))
