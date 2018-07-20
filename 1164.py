n = int(input())
for i in range(n):
    soma = 0
    x = int(input())
    for c in range(1 ,x):
        if x%c==0:
            soma+=c
    if soma == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
        
