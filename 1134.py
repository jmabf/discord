a = 0
g = 0
d = 0
i = 0
while i!=4:
    i = int(input())
    if i == 1:
        a += 1
    elif i == 2:
        g += 1
    elif i == 3:
        d += 1
print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(a,g,d))
