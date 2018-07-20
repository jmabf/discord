s = 1
n = 1
r = 1
for x in range(2, 21):
    s += 2
    n *= 2
    r += s/n 
print('{:.2f}'.format(r))
