n = int(input())
lista = [ ]
i = 0
while i<n:
    x, y = [int(x) for x in input().split()]
    if y == 0:
        lista.append('divisao impossivel')
    else:
        divisao = x/y
        lista.append(divisao)
    i+=1
for x in lista:
    print(x)
