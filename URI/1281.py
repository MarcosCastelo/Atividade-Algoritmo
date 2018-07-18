n = int(input())

for i in range(n):
    produtos = []
    total = 0
    m = int(input())

    for j in range(m):
        produtos += [input().split()]

    p = int(input())

    for j in range(p):
        compras = input().split()
        for k in range(len(produtos)):
            if produtos[k][0] == compras[0]:
                total += float(produtos[k][1]) * int(compras[1])

    print("R$ %.2f" % total)
