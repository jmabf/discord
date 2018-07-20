i = []
for x in range(20):
    n = int(input())
    i.append(n)
for c in range(20):
    print('N[{}] = {}'.format(c,i[19-c]))
