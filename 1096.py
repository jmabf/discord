i = 0
j = 0
if i==0 and j == 0:
    i+=1
    j+=7
    print('I={} J={}'.format(i,j))
while j>5:
    j-=1
    print('I={} J={}'.format(i,j))
    if i == 9 and j == 13:
        break
    if j == i+4:
        i+=2
        j += 4
        print('I={} J={}'.format(i,j))

