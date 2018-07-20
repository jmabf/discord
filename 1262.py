while True:
    try:
        lista = list(input())
        n = int(input())
        i = 0
        p = 0
        for x in lista:
            if x == 'W':
                if i>0:
                    p+=1
                p += 1
                i = 0
            elif x == 'R':
                i+=1
                if i == n:
                    p+=1
                    i = 0
        if i>0:
            p+=1
        print(p)
    except EOFError:
        break
