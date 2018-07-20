n1= float(input())
n2= float(input())
n3= float(input())
n4= float(input())
n5= float(input())
lista = [n1,n2,n3,n4,n5,]
par=0
impar=0
pos=0
neg=0
for x in lista:
    if x%2==0:
        par+=1
    elif x%2==1:
        impar+=1
    if x>0:
        pos+=1
    elif x<0:
        neg+=1
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(par,impar,pos,neg))

