n = int(input())
x = [int(i) for i in input().split()]
menor = x[0]
pos = 0

for i in range(n):
    if x[i] < menor:
        menor = x[i]
        pos = i

print("Menor valor:",menor)
print("Posicao:",pos)
