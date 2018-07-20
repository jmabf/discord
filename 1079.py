n = int(input())
i=0
lista = []
while i<n:
    notas = input().split()
    a = float(notas[0])
    b = float(notas[1])
    c = float(notas[2])
    media = ((a*2)+(b*3)+(c*5))/10
    lista.append(media)
    i+=1
for x in lista:
    print('{:.1f}'.format(x))
