#A-Z = 65-90; a-z = 97-122


mensagem = []
criptografia = []
n = int(input())
for i in range(n):
    mensagem.append(input())

for frase in mensagem:
    str_aux = ""
    primeira = ""
    segunda = ""
    terceira = ""
    
    for letra in frase:
        if(letra.isalpha()):
            primeira += chr(ord(letra) + 3)
        else:
            primeira += letra
            
    segunda = primeira[::-1]
    
    for i in range(len(segunda)//2,len(segunda),1):
        terceira += chr(ord(segunda[i])-1)

    str_aux = segunda[:len(segunda)//2] + terceira
        
    criptografia.append(str_aux)

for frase in criptografia:
    print(frase)
