fibo=[0,1]
p=0
s=1
for i in range(60):
    t=s+p
    fibo.append(t)
    p=s
    s=t
n = int(input())
for c in range(n):
    x = int(input())
    print('Fib({}) = {}'.format(x, fibo[x]))
