while True:
    num1,num2 = input().split()
    if num1=='0'and num2=='0':
        break
    else:
        numf = str(int(num1)+int(num2))
        numf=numf.replace('0' , '')
        print(numf)
    
