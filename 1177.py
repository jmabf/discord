n = int(input())
i = -1
l = []
for x in range(1000):
    i+=1
    if i == n:
        i = 0
    l.append(i)
    print('N[{}] = {}'.format(x,l[x]))
    
