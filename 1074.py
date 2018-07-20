n = int(input())
i = 0
lista= [ ]
while i<n:
    c = int(input())
    lista.append(c)
    i+=1
for x in lista:
    if x%2==0 and x>0:
        print('EVEN POSITIVE')
    elif x%2==1 and x>0:
        print('ODD POSITIVE')
    elif x%2==0 and x<0:
        print('EVEN NEGATIVE')
    elif x%2==1 and x<0:
        print('ODD NEGATIVE')
    else:
        print('NULL')
