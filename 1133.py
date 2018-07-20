x = int(input())
y = int(input())
lista = [x,y]
lista_numeros = [ ]
lista.sort()
n1 = lista[0]
n2 = lista[1]
for c in range(n1+1, n2):
    if c%5 == 2 or c%5 == 3:
        lista_numeros.append(c)
for c in lista_numeros:    
    print(c)
