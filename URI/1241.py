n = int(input())
for i in range(n):
    a, b = input().split()
    if b in a[len(a)-len(b):]:
        print("encaixa")
        print(a[len(a)-len(b):])
    else:
        print("nao encaixa")
        print(a[len(a)-len(b):])
