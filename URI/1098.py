I = 0

while I <= 20:
    for i in range(1,4):
        i += I/10
        if i%1!=0:
            print("I=%.1f J=%.1f" % (I/10,i))
        else:
            print("I=%d J=%d" % (I/10,i))
    J = 0
    I += 2


