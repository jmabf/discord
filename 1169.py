for x in range(int(input())):
    n = int(input())
    kilos = ((2**n-1)//12)//1000
    print('{:.0f} kg'.format(kilos))
    
