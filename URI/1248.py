n = int(input())
for i in range(n):
    dieta = input()
    cafe = input()
    almoco = input()
    refeicoes = cafe+almoco
    cheater = False

    for prato in refeicoes:
        achou = False
        for i in range(len(dieta)):
            if prato == dieta[i]:
                achou = True
        if not achou:
            cheater = True
        else:
            dieta = dieta.replace(prato,"")

    if cheater:
        print("CHEATER")
    else:
        print(''.join(sorted(dieta)))
            
        
