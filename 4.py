def check_net(N):
    return (N >= 3) and (N % 2 == 0)

count = 0
while True:
    N = int(input())
    if N == 0:
        break
    if check_net(N):
        count += 1

print(count)