lista = []
resultado =''
soma = 0
while True:
    x = input().split()
    x.sort()
    n1 = int(x[0])
    n2 = int(x[1])
    if n1<1 or n2<1:
        break
    else:
        for c in range(n1, n2+1):
            soma+=c
            resultado += str(c) + ' '
        print('{}Sum={}'.format(resultado, soma))
        resultado = ''
        soma = 0
        
        
    
