while True:
    try:
        entrada = input()
        I_fechado = True
        B_fechado = True
        for letra in entrada:
            if "_" in letra:
                if I_fechado:
                    letra = letra.replace("_","<i>")
                    I_fechado = False
                else:
                    letra = letra.replace("_","</i>")
                    I_fechado = True
                    
            if "*" in letra:
                if B_fechado:
                    letra = letra.replace("*","<b>")
                    B_fechado = False
                else:                
                    letra = letra.replace("*","</b>")
                    B_fechado = True

            print(letra, end="")
        print("")
    except EOFError:
        break
