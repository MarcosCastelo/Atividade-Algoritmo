par = []
impar = []
for j in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) >= 5:
        for i in range(len(par)):
            print("par[%d] = %d" % (i, par[i]))
        par = []
    if len(impar) >= 5:
        for i in range(len(impar)):
            print("impar[%d] = %d" % (i, impar[i]))
        impar = []
        
for i in range(len(impar)):
    print("impar[%d] = %d" % (i, impar[i]))
impar = []

for i in range(len(par)):
    print("par[%d] = %d" % (i, par[i]))
par = []
