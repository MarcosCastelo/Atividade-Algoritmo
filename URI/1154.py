i = int(input())
cont = 0
soma = 0

while i > 0:
    soma += i
    i = int(input())
    cont += 1

media = soma / cont

print("%.2f" % media)
