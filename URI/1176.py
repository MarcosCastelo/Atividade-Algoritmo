n = int(input())
fibonacci = [0]
num = 0
aux = 1
for i in range(60) :
    aux2 = num
    num += aux
    aux = aux2
    fibonacci.append(num)

for num in range(n):
    x = int(input())
    print("Fib(%d) = %d" % (x, fibonacci[x]))
