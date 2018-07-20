soma = 0
i = 0
lista = [ ]
while True:
    if i == 2:
        break
    n = float(input())
    if 0<=n<=10:
        soma += n
        i += 1
    else:
        lista.append('nota invalida')
lista.append('media = {:.2f}'.format(soma/2))
for x in lista:
    print(x)

