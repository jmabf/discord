n1,n2 = list(map(int,input().split()))
i = 1
for x in range(1,(int((n2/n1))+1)):
    r = ""
    for y in range(n1):
        r += str(i) + " "
        i += 1
    print(r[:-1])
