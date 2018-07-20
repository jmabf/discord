for x in range(int(input())):
    nomes= input().split()
    numeros= input().split()
    p1 = nomes[0],nomes[1]
    p2 = nomes[2],nomes[3]
    soma = int(numeros[0])+int(numeros[1])
    lista= p1,p2
    if soma%2==1:
        for y in range(len(lista)):
            if lista[y][1] == 'IMPAR':
                print(''.join(lista[y][0]))
    else:
        for y in range(len(lista)):
            if lista[y][1] == 'PAR':
                print(''.join(lista[y][0]))
