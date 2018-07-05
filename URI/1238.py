n = int(input())
for i in range(n):
    primeiro, segundo = input().split()
    combinado = ""
    if len(segundo) > len(primeiro):
        for i in range(len(primeiro)):
            combinado += primeiro[i] + segundo[i]
        combinado += segundo[len(primeiro):]
    else:
        for i in range(len(segundo)):
            combinado += primeiro[i] + segundo[i]
        combinado += primeiro[len(segundo):]
    print(combinado)
