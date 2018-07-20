n=int(input())
for n in range(n):
    anos=0
    PA,PB,G1,G2=[int(x) for x in input().split()]
    while PA<PB and anos<=100:
        anos+= 1
        PA+=int(PA*(G1/100))
        PB+=int(PB*(G2/100))
    if anos>100:
        print('Mais de 1 seculo')
    else:
        print('{} anos'.format(anos))
