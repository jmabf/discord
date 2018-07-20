x = int(input())
y = int(input())
lista = [x,y]
lista.sort()
soma = 0
n1 = lista[0]
n2 = lista[1]
for c in range(n1, n2+1):
    if c%13!=0:
        soma+=c
print(soma)
