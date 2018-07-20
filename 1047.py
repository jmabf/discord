a,b,c,d = [int(x) for x in input().split()]
if a>c:
     c+=24
elif a==c and b>d:
    c+=24
elif a==c and b==d:
    c+=24
x= c-a
if b>d:
    d+=60
    x-=1
y = d-b
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(x,y))
