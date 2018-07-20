for x in range(int(input())):
    soma = 0
    p = 0
    for y in range(int(input())):
        e = 0
        n = input().upper()
        for l in n:
            soma+= ord(l)-65+p+e
            e+=1
        p+=1
        
    print(soma)
