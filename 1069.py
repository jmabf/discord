for x in range(int(input())):
    dia = input()
    dia = dia.replace('.', '')
    i= 0
    while True:
        if '<>' in dia:
            y = dia.find('<>')
            dia = dia[0:y]+dia[y+2:]
            i+=1
        else:
            break
    print(i)
            
