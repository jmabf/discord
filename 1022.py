for x in range(int(input())):
    ope = input().split()
    den1 = int(ope[2])
    den2 = int(ope[6])
    num1 = int(ope[0])
    num2 = int(ope[4])
    if ope[3] == '+':
        num_n = num1*den2+num2*den1
        den = den1*den2
    elif ope[3] == '-':
        num_n = num1*den2-num2*den1
        den = den1*den2
    elif ope[3] == '*':
        num_n = num1*num2
        den = den1*den2
    elif ope[3] == '/':
        num_n = num1*den2
        den = num2*den1
    fracao = '{:.0f}/{:.0f}'.format(num_n, den)
    num_f = num_n
    den_f = den
    while True:
        if num_f % 2 == 0 and den_f%2==0:
            num_f = num_f/2
            den_f = den_f/2
        elif num_f%3==0 and den_f%3==0:
            num_f = num_f/3
            den_f = den_f/3
        elif num_f%5 == 0 and den_f%5 == 0:
            num_f = num_f/5
            den_f = den_f/5
        elif num_f%7 == 0 and den_f%7 == 0:
            num_f = num_f/7
            den_f= den_f/7
        else:
            break
    fracao_f = '{:.0f}/{:.0f}'.format(num_f,den_f)
    print('{} = {}'.format(fracao, fracao_f))
