i = 0
soma = 0
while True:
    age =int(input())
    if age>=0:
        soma+= age
        i+= 1
    else:
        break
print('{:.2f}'.format(soma/i))
