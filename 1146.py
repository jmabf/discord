while True:
    n= int(input())
    if n == 0:
        break
    lista = ''
    for c in range(1, n+1):
        if c == n:
            lista+= str(c)
        else:
            lista += str(c) + ' '
    print(lista)
        
