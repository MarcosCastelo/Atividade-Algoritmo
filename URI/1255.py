n = int(input())
for j in range(n):
    mensagem = input()
    aux = [[]]
    for i in range(len(mensagem)):
        if mensagem[i].isalpha():
            aux.append([mensagem.count(mensagem[i]),mensagem[i]])            
    aux.sort(reverse=True)    
    
    maior = [aux[x][0] for x in range(len(aux)-1)]
    letra = [aux[x][1] for x in range(len(aux)-1)]

    for i in range(len(letra)-1):
        if letra[i] == letra[i+1]:
            letra[i+1] = "$"
            maior[i+1] = "$"

    print(maior.remove("$"),letra)
    
            
    print("")
        
        
            
                
