d,n = input().split(" ")
v = []

while d != '0' and n != '0':
    v.append(n.replace(d,''))
    d,n = input().split(" ")

for i in v:
    if i != "":
        if int(i) != 0:
            print(int(i))
        else:
            print(0)
    else:
        print(0)

