import sys

N = int(sys.stdin.readline().split()[0])
container = []
for i in range(N):
    container.append(sys.stdin.readline().split()[0])

container = list(set(container))

container.sort(key = lambda x : (len(x),x))

for i in range(len(container)):
    print(container[i])