while True:
    n = int(input())
    i= 0
    soma= 0
    if n!=0:
        while i<5:
            for x in range(n , n+10):
                if x%2==0:
                    soma+=x
                    i+=1
    else:
        break
    print(soma)
            
            
            
