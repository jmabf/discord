i = 0
tipo = int(input())
chas = [int(x) for x in input().split()]
for x in chas:
    if x ==tipo:
        i+=1
print(i)
