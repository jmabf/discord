n = int(input())
for c in range(n):
    soma = 0
    x, y = [int(x) for x in input().split()]
    for l in range(y):
        while x%2==0:
            x+=1
        soma+=x
        x+=1
    print(soma)
