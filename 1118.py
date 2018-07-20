soma = 0
i = 0
lista = [ ]
novo_c= 0
while True:
    while i == 2:
        novo_c = int(input('novo calculo (1-sim 2-nao)\n'))
        if novo_c == 2:
            break
        elif novo_c == 1:
            soma = 0
            i = 0
            lista = [ ]
    if novo_c == 2:
        break
    n = float(input())
    if 0<=n<=10:
        soma += n
        i += 1
    else:
        lista.append('nota invalida')
    if i == 2:
        lista.append('media = {:.2f}'.format(soma/2))
        for x in lista:
            print(x)
