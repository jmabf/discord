while True:
    try:
        input()
        n = input().split()
        v = 0
        maior = 0
        for x in n:
            if int(x)>= maior:
                maior = int(x)
        if maior >= 20:
            v = 3
        elif 10<=maior<20:
            v = 2
        elif maior<10:
            v = 1
        print(v)
    except EOFError:
        break
