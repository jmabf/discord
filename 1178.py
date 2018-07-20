n = float(input())
lista = []
for x in range(100):
    lista.append(n)
    n/=2
    print('N[{}] = {:.4f}'.format(x,lista[x]))
