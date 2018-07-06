def is_sorted(lista):
    new_lista = lista[:]
    new_lista.sort()
    if new_lista == lista:
        return True
    else:
        return False

t = [1, 2, 2]
u = ["b", "a"]

print(is_sorted(t))
print(is_sorted(u))
