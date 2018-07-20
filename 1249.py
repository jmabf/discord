while True:
    try:
        texto = input()
        qte = 13
        t_new = ''
        for x in texto:
            if 65<=ord(x)<=90:
                if ord(x)+13>90:
                    t_new += str(chr(ord(x)-13))
                else:
                    t_new += str(chr(ord(x)+13))
            elif 97<=ord(x)<=122:
                if ord(x)+13>122:
                    t_new += str(chr(ord(x)-13))
                else:
                    t_new += str(chr(ord(x)+13))
            else:
                t_new += str(x)
        print(t_new)
    except EOFError:
        break
