while True:
    try:
        v = float(input())
        d = float(input())
        r=d/2
        pi=3.14
        ar=(r**2)*pi
        h=v/ar
        print('ALTURA = {:.2f}'.format(h))
        print('AREA = {:.2f}'.format(ar))
    except EOFError:
        break
