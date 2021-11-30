import sys

T = int(sys.stdin.readline().split()[0])

for t in range(T):
    k = int(sys.stdin.readline().split()[0])
    n = int(sys.stdin.readline().split()[0])
    
    basefloor = [x for x in range(1,n+1)]
    target = [x for x in range(1,n+1)]
    
    for fl in range(k):
        for i in range(n):
            target[i] = sum(basefloor[:i+1])
        basefloor = target[:len(target)]
    print(target[n-1])