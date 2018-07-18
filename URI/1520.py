while True:
    try:
        n = input()
        if n != '':
            n = int(n)
            lista = []
            for i in range(n):
                tam = list(map(int, input().split()))
                for j in range(tam[0],tam[1]+1):
                    lista.append(j)

            lista.sort()
            num = int(input())
            if num in lista:
                inicio = None
                fim = None

                for i in range(len(lista)):
                    if inicio == None:
                        if lista[i] == num:
                            inicio = i
                    else:
                        if lista[i] == num:
                            fim = i
                if fim == None:
                    fim = inicio
                print("%d found from %d to %d" % (num, inicio, fim))
            else:
                print(num, "not found")

    except EOFError:
        break