n = int(input())
k=[]
for x in range(1,n):
    for y in range(1,n):
        if ((x**2)+(y**2))==n:
            k.append(x)
            k.append(y)
k=set(k)
print(round(len(k)/2), k)

'''n = int(input())
count=0
for x in range(1,(int(n**0.5))+1):
    y=int((n-x**2)**0.5)
    if ((x**2)+(y**2))==n and y>=x:
        count+=1
print(count)'''

