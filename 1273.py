i = 0
while True:
    n = int(input())
    if n == 0:
        break
    tam = 0
    lista = []
    for x in range(n):
        nome = input()
        if len(nome) > tam:
            tam = len(nome)
        lista.append(nome)
    if i == 1:
        print('')
    for y in lista:
        print(y.rjust(tam, ' '))
    i = 1
