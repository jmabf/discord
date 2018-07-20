n = int(input())
for i in range(n):
    soma = 0
    x = int(input())
    for c in range(1 ,x):
        if x%c==0:
            soma+=1
    if soma == 1:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
        
