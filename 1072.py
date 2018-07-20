nx = int(input())
i = 0
lista = [ ]
while i<nx:
    c = int(input())
    lista.append(c)
    i+=1
dentro = 0
fora = 0
for x in lista:
    if 10>=x<=20:
        dentro+=1
    else:
        fora+=1
print('{} in\n{} out'.format(dentro, fora))
        
    
