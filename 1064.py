n1= float(input())
n2= float(input())
n3= float(input())
n4= float(input())
n5= float(input())
n6= float(input())
lista = [n1,n2,n3,n4,n5,n6]
y=0
soma=0
for x in lista:
    if x>=0:
        y+=1
        soma+=x
print('{} valores positivos'.format(y))
print('{:.1f}'.format(soma/y))
