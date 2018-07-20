preco = 0
for x in range(int(input())):
    n,q = [int(x) for x in input().split()]
    if n == 1001:
        preco += q*1.5
    elif n ==1002:
        preco += q*2.5
    elif n ==1003:
        preco +=q*3.5
    elif n ==1004:
        preco+=q*4.5
    elif n ==1005:
        preco+=q*5.5
print('{:.2f}'.format(preco))
