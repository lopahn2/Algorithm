import sys

N = int(sys.stdin.readline().split()[0])

container = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    container.append((x,y))
    
container.sort()

for i in range(len(container)):
    print(container[i][0], container[i][1])
