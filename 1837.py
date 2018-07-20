a,b = [int(x) for x in input().split()]
if a>0 and b<0:
    a = abs(a)
    b = abs(b)
    print('-{} {}'.format(a//b,a%b))
else:
    print('{} {}'.format(a//b,abs(a%b)))
