n=input().strip()
if 'e' in n:
    n=n[:n.find('e')]
print('{}'.format(n[::-1]))
