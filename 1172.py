i = []
for x in range(10):
    n = int(input())
    if n <=0:
        n = 1
    i.append(n)
    print('X[{}] = {}'.format(x, n))
