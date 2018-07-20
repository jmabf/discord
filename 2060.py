n = int(input())
lista = [int(x) for x in input().split()]
dois= 0
tres=0
quatro=0
cinco=0
for x in lista:
    if x%2==0:
        dois+=1
    if x%3==0:
        tres+=1
    if x%4 ==0:
        quatro+=1
    if x%5==0:
        cinco+=1
print('{} Multiplo(s) de 2'.format(dois))
print('{} Multiplo(s) de 3'.format(tres))
print('{} Multiplo(s) de 4'.format(quatro))
print('{} Multiplo(s) de 5'.format(cinco))
