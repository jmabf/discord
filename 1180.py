x = int(input())
n = input().split()
i = 0
p = 0
menor = 1000
for c in n:
    if int(c)<menor:
        menor = int(c)
        p = i
    i+=1
print('Menor valor: {}\nPosicao: {}'.format(menor,p))
        
        
        
