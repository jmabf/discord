lista = [ ]
while True:
    n = int(input())
    lista.append(n)
    if n == 2002:
        break
for x in lista:
    if x == 2002:
        print('Acesso Permitido')
    else:
        print('Senha Invalida')
