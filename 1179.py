par = []
impar = []
for x in range(15):
    n = int(input())
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    if len(par)==5:
        for v in range(5):
            print('par[{}] = {}'.format(v,par[v]))
        par =[]
    if len(impar)==5:
        for v in range(5):
            print('impar[{}] = {}'.format(v,impar[v]))
        impar=[]
if len(impar)>0:
    i = 0 
    for v in impar:
        print('impar[{}] = {}'.format(i,v))
        i+=1
if len(par)>0:
    i = 0 
    for v in par:
        print('par[{}] = {}'.format(i,v))
        i+=1
