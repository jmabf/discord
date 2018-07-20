n = int(input())
for x in range(n):
    led = 0
    num = str(input())
    for l in num:
        if l == '1':
            led+= 2
        if l == '2':
            led+= 5
        if l == '3':
            led+= 5
        if l == '4':
            led+= 4
        if l == '5':
            led+= 5
        if l == '6':
            led+= 6
        if l == '7':
            led+= 3
        if l == '8':
            led+= 7
        if l == '9':
            led+= 6
        if l == '0':
            led+= 6
    print('{} leds'.format(led))
