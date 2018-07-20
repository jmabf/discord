grenais = 0
vit_g = 0
vit_i = 0
empate = 0
i = 0
venceu = 0
while i != 2:
    inter, gremio = [int(x) for x in input().split()]
    if inter > gremio:
        vit_i += 1
    elif gremio > inter:
        vit_g += 1
    else:
        empate += 1
    i = int(input('Novo grenal (1-sim 2-nao)\n'))
    grenais += 1
if vit_i > vit_g:
    venceu = 'Inter venceu mais'
else:
    venceu = 'Gremio venceu mais'
print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}\n{}'.format(grenais,vit_i,vit_g,empate,venceu))
