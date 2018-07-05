while True:
    try:
        tag = input()
        cod = input()
        mensagem = input()

        flag = 1
        pedacos = []
        for i in range(len(mensagem))
        inicio = 0
        fim = 0
            if flag == 1 and mensagem[i] == "<":
               inicio = i
               flag = 2
            elif mensagem[i] == "<":
                flag = 0
                
            if flag == 2 and mensagem[i] == ">":
                fim = i+1
                flag = 1
            elif mensagem[i]  == ">"
                flag = 1
                
            
        
    except EOFError:
        break
