n = int(input())
i = 0
c=0
r=0
s=0
while i<n:
    v = input().split()
    t = v[1].upper()
    q = int(v[0])
    if t == 'C':
        c+=q
    elif t == 'R':
        r+=q
    elif t == 'S':
        s+=q
    i+=1
total = c+r+s
porc_c = 100*c/total
porc_r = 100*r/total
porc_s = 100*s/total
print('Total: {} cobaias\n'
      'Total de coelhos: {}\n'
      'Total de ratos: {}\n'
      'Total de sapos: {}\n'
      'Percentual de coelhos: {:.2f} %\n'
      'Percentual de ratos: {:.2f} %\n'
      'Percentual de sapos: {:.2f} %'.format(total, c, r,s,porc_c,porc_r,porc_s))
