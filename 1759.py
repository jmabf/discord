n = int(input())
i= 0
plvr = ''
for x in range(n):
    if i == 0:
        plvr += 'Ho '
    elif i ==1:
        plvr+= 'Ho'
    if x == n-2:
        i = 1
print(plvr+'!')
