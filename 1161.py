def fat(numero):
    fatorial = 1
    while numero!=0:
        fatorial *= numero
        numero-=1
    return fatorial
while True:
    try:
        m,n= [int(x) for x in input().split()]
        soma = fat(m)+ fat(n)
        print(soma)
    except EOFError:
        break
        
