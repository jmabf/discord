import math
while True:
    try:
        n1 = str(input())
        n2 = float(input())
        ponto = n1.find('.')
        if ponto == len(n1)-1:
            n1+= '0'
        n1_n = float(n1[ponto:])
        if n1_n > n2:
            n1 = math.ceil(float(n1))
        else:
            n1 = math.floor(float(n1))
        print(n1)
    except EOFError:
        break
        
