while True:
    try:
        texto = input().lower().split()
        lista = []
        i = 0
        for x in range(len(texto)-1):
            if texto[x][0] not in lista:
                if texto[x][0] == texto[x+1][0]:
                    i+=1
                    lista.append(texto[x][0])

        print(i)
    except EOFError:
        break
                    
