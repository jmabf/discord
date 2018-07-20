for x in range(int(input())):
    anos = 2015
    n = int(input())
    anos = anos-n
    if anos<0:
        print(str(abs(anos)+1)+' A.C.')
    elif anos == 0:
        print('1 A.C.')
    else:
        print(str(anos)+' D.C.')
