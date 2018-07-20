for l in range(int(input())):
    input()
    nome = input().split()
    pres = input().split()
    lista = []
    i = 0
    for x in range(len(nome)):
        nome_r = nome[x]
        tam = len(pres[x])
        for y in pres[x]:
            if y == 'P':
                i+=1
            elif y == 'M':
                tam -=1
            else:
                pass
        if i<(3*tam)/4:
            lista.append(nome_r)
        i = 0
    resposta =' '.join(lista)
    print(resposta)

