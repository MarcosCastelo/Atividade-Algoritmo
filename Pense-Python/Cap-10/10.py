def in_bisect(lista,item):
    if item in lista:
        return lista.index(item)
    else:
        return None

t = [1,2,3,4,5,6]

print(in_bisect(t,4))
