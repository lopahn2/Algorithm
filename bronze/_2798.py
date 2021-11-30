import sys

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

container = []
ans = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            container.append(cards[i] + cards[j] + cards[k])

for i in range(len(container)):
    temp = M - container[i]
    if temp >= 0:
        ans.append(container[i])
    
print(max(ans))
    