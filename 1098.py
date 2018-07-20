i = 0
j = 0
while i==0 and j <3:
    j+=1
    print('I={} J={}'.format(i,j))
if j == i+3:
        i+=0.2
        j = 1+i
        print('I={} J={}'.format(i,j))

while j<i+3:
    if i == 2.0 and j == 5.0:
        break
    j+=1
    print('I={} J={:.1f}'.format(i,j))
    if j == i+3:
        i+=0.2
        j = 1+i
        print('I={} J={:.1f}'.format(i,j))
