repeticoes = int(input())
for i in range(repeticoes):
    cripta = input()
    chave = int(input())
    for letra in cripta:
        pos_letra = ord(letra) - 65
        decript = pos_letra - chave
        if decript < 0:
            decript = 26 - abs(decript)
        print(chr(decript + 65),end="")
    print("")
