while True:
    try:
        palavras = input().split()

        tamanho = 0
        media = 0
        for palavra in palavras:
            for letra in palavra:
                if not letra.isalpha():
                    tamanho -= 1
            tamanho += len(palavra)
        if len(palavras) > 1:
            media = tamanho//len(palavras)
        elif len(palavras) == 1:
            media = 1
        if media <= 3 and media > 0:
            print(250)
        elif media > 3 and media <= 5:
            print(500)
        elif media > 5:
            print(1000)
    except EOFError:

        break
