while True:
    try:
        texto = input()
        texton = ''
        i = 0
        b = 0
        for x in texto:
            if x == '_':
                if i%2 == 0:
                    texton += '<i>'
                else:
                    texton += '</i>'
                i+=1
            elif x == '*':
                if b%2 == 0:
                    texton += '<b>'
                else:
                    texton += '</b>'
                b+=1
            else:
                texton += str(x)
        print(texton)
    except EOFError:
        break
