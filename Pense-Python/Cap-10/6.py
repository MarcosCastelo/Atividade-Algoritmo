def is_anagram(a,b):
    lista_a = list(a)
    lista_b = list(b)
    lista_a.sort()
    lista_b.sort()

    if lista_a == lista_b:
        return True
    else:
        return False

a = "anagrama"
b = "amagrana"

print(is_anagram(a,b))
