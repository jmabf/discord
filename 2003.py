while True:
    try:
        acordou = input()
        hora = int(acordou[0])
        minutos = int(acordou[2:])
        atraso = 0
        if hora+1>=8:
            atraso = ((hora+1)-8)*60+minutos
        print('Atraso maximo: {}'.format(atraso))
    except EOFError:
        break
