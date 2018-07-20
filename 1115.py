lista = [ ]
while True:
    x, y = [int(x) for x in input().split()]
    if x>0 and y>0:
        lista.append('primeiro')
    elif x>0 and y<0:
        lista.append('quarto')
    elif x<0 and y<0:
        lista.append('terceiro')
    elif x<0 and y>0:
        lista.append('segundo')
    elif x == 0 or y == 0:
        break
for x in lista:
    print(x)
