aluno_f = 0
nota_f = 0
for x in range(int(input())):
    aluno,nota = [float(x) for x in input().split()]
    if nota>nota_f:
        aluno_f = int(aluno)
        nota_f = nota
if nota_f<8:
    print('Minimum note not reached')
else:
    print(aluno_f)
