n = float(input())
print("N[0] = %.4f" % n)
for i in range(1,100):
    n /= 2
    print("N[%d] = %.4f" % (i, n))
