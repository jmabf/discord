while True:
    try:
        plvr = str(input())
        i = 0
        plvr_n = ''
        for x in plvr:
            if 65<=ord(x)<=90 or 97<=ord(x)<=122:
                if i%2 == 0:
                    plvr_n += x.upper()
                else:
                    plvr_n += x
                i+=1
            else:
                plvr_n += x
        print(plvr_n)
    except EOFError:
        break
