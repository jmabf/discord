h,t,f = [int(x) for x in input().split()]
h_chegada = h+t
if h_chegada>= 24:
    h_chegada-= 24
h_final = h_chegada + f
if h_final<0:
    h_final+=24
print(h_final)
