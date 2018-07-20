x= int(input())
y= int(input())
if x>y:
    lista= range(y+1,x)
else:
    lista= range(x+1, y)
soma=0
for c in lista:
    if c%2==1:
        soma+=c
print(soma)
        
