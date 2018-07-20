antigo,novo = [float(x) for x in input().split()]
taxa = ((novo*100)/antigo)-100
print('{:.2f}%'.format(taxa))
