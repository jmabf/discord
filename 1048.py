salario = float(input())
n_salario = 0
percentual = 0
if salario<=400:
    n_salario = salario*0.15+salario
    percentual = 15
    reajuste = n_salario-salario
elif 400<salario<=800:
    n_salario = salario*0.12+salario
    percentual = 12
    reajuste = n_salario-salario
elif 800<salario<=1200:
    n_salario = salario*0.1+salario
    percentual = 10
    reajuste = n_salario-salario
elif 1200<salario<=2000:
    n_salario = salario*0.07+salario
    percentual = 7
    reajuste = n_salario-salario
elif 2000<salario:
    n_salario = salario*0.04+salario
    percentual = 4
    reajuste = n_salario-salario
print('Novo salario: {:.2f}\n'
      'Reajuste ganho: {:.2f}\n'
      'Em percentual: {} %'.format(n_salario, reajuste, percentual))
