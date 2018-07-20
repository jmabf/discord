i = 0
while True:
    lista_n = []
    tam = 0
    n = int(input())
    if n == 0:
        break
    for p in range(n):
        frase_n =' '
        lista = []
        frase = input().split()
        frase_n = frase_n.join(frase)
        lista_n.append(frase_n)
        if len(frase_n)>tam:
            tam=len(frase_n)
    if i == 1:
        print('')
    for x in lista_n:
        print(x.rjust(tam, ' '))
    i=1
        
