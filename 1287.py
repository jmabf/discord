while True:
    try:
        plvr = str(input())
        plvr_n =''
        i = 0
        for x in plvr:
            if x == 'O' or x == 'o':
                plvr_n += '0'
            elif x == 'l' or x == 'L':
                plvr_n += '1'
            elif x == ',' or x == ' ':
                pass
            else:
                plvr_n += str(x)
        for y in plvr_n:
            if not 48<=ord(y)<=57:
                plvr_n = 'error'
                i+=1
        try:        
            if str(plvr_n) == '' and i==0:
                plvr_n = 'error'
            elif int(plvr_n) == 0 and i ==0:
                plvr_n = 0
            elif int(plvr_n)>2147483647 or int(plvr_n)<0:
                plvr_n = 'error'
        except ValueError:
            plvr_n = 'error'
        try:
            print(int(plvr_n))
        except ValueError:
            print(plvr_n)
    except EOFError:
        break
