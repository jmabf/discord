n = int(input())
for x in range(n):
    dieta = list(input())
    cafe = input()
    almoco = input()
    comeu = []
    falta ='' 
    for l in cafe:
        comeu.append(l)
    for k in almoco:
        comeu.append(k)
    for m in dieta:
        if m in dieta and m not in comeu:
            falta += str(m)
    for y in comeu:
        if y not in dieta:
            falta = 'CHEATER'
            break
    if falta == 'CHEATER':
        print(falta)
    else:
        print(''.join(sorted(falta)))
