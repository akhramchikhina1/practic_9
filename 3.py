n = int(input())
for i in range(int(n**0.5),2,-1):
    if (n%i)==0:
        print(i)