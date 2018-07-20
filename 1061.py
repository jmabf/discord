diai= input().split()
tempoi= input().split()
diaf= input().split()
tempof=input().split()

d1= int(diai[1])
h1 = int(tempoi[0])
m1 = int(tempoi[2])
s1 = int(tempoi[4])
t1 = (d1*86400)+(h1*3600)+(m1*60)+(s1)

d2 = int(diaf[1])
h2 = int(tempof[0])
m2 = int(tempof[2])
s2 = int(tempof[4])
t2 = (d2*86400)+(h2*3600)+(m2*60)+(s2)


tf = t2-t1
df = tf//86400
r1 = tf%86400
hf = r1//3600
r2 = r1%3600
mf = r2//60
sf = r2%60

print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(df,hf,mf,sf))

