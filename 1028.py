from fractions import gcd
for x in range(int(input())):
    a,b = [int(x) for x in input().split()]
    print(gcd(a,b))
