lista = [ ]
while True:
    x, y = [int(x) for x in input().split()]
    if x > y:
        lista.append('Decrescente')
    elif y>x:
        lista.append('Crescente')
    else:
        break
for x in lista:
    print(x)
