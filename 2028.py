i=0
while True:
    try:
        lista= []
        n= input()
        for x in range(int(n)+1):
            if x== 0:
                lista.append(str(x))
            else:
                for y in range(x):
                    lista.append(str(x))
                
        frase=' '.join(lista)
        i+=1
        if len(lista)==1:
            print('Caso {}: {} numero'.format(i,len(lista)))
        else:
            print('Caso {}: {} numeros'.format(i,len(lista)))
        print(frase)
        print()
    except EOFError:
        break
