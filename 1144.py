n = int(input())
y = 1
for x in range(n):
    print('{} {} {}\n{} {} {}'.format(y,y**2,y**3,y,(y**2)+1,(y**3)+1))
    y+=1
