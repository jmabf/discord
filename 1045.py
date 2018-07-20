x,y,z = [float(x) for x in input().split()]
lista = [x,y,z]
lista.sort()
a = lista[2]
b = lista[1]
c = lista[0]
if a>=b+c:
    print('NAO FORMA TRIANGULO')
elif (a**2) == (b**2)+(c**2):
    print('TRIANGULO RETANGULO')
elif (a**2) > (b**2)+(c**2):
    print('TRIANGULO OBTUSANGULO')
elif (a**2) < (b**2)+(c**2):
    print('TRIANGULO ACUTANGULO')
if a==b==c:
    print('TRIANGULO EQUILATERO')
elif a==b and a!=c or a==c and a!=b or b==c and b!=a:
    print('TRIANGULO ISOSCELES')
