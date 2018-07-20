from collections import Counter
for n in range(int(input())):
    i = 0
    texto = input()
    texto = texto.replace(' ','')
    lista = list(texto.lower())
    mais = Counter(lista).most_common(10)
    plvr = ''
    for x in range(len(mais)):
        if i ==0 and 97<=ord(mais[x][0])<=122:
            plvr+= str(mais[x][0])
            i = mais[x][1]
        elif mais[x][1] == mais[0][1] and mais[x][1] == i:
            plvr+= str(mais[x][0])
    plvr_n= ''.join(sorted(plvr))
    plvr = ''
    for l in plvr_n:
        if not 97<=ord(l)<=122:
            pass
        else:
            plvr+= l
    print(plvr)
