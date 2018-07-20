i = []
for x in range(100):
    n = float(input())
    i.append(n)
    if n<=10:
        print('A[{}] = {:.1f}'.format(x, n))
