n = int(input())
lista = range(1 , n+1)
for x in lista:
    if x%2==0:
        c = x*x
        print('{}^2 = {}'.format(x, c))
        
