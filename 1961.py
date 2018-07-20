pulo,n = [int(x) for x in input().split()]
canos = [int(x) for x in input().split()]
morreu = False
for x in range(n-1):
    if canos[x+1]-canos[x]>1:
        if canos[x+1]-canos[x]>pulo:
            morreu = True
if morreu:
    print('GAME OVER')
else:
    print('YOU WIN')
