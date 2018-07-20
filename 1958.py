n = float(input())
if n == 0 and (str(n)[0] =="0" or str(n)[0]=='+'):
    print('+%.4E'%n)
elif n>0:
    print('+%.4E'%n)
else:
    print('%.4E'%n)
