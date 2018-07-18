def tem_depois(sequencia, subsequencia):
    comparador = sequencia
    compara = subsquencia
    cont = 0
    for i in range(len(compara)):
        for j in range(len(comparador)):
            if compara[i] == comparador[j]:
                comparador = comparador[j+1:]
                cont += 1
                break

    if cont >= len(compara):
        return "Yes"
    else:
        return "No"


n = int(input())

for i in range(n):
    sequencia = input()
    n_subsquencia = int(input())

    for casos in range(n_subsquencia):
            subsquencia = input()
            print(tem_depois(sequencia, subsquencia))
