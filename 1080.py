i = 1
maior = 0
posiçao =0
for e in range(100):
    x = int(input())
    if x > maior:
        maior = x
        posiçao = i
    i += 1
print(maior)
print(posiçao)
