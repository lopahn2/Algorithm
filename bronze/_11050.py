import sys

def fac(n):
    count = 1
    for i in range(1,n+1):
        count *= i
    return count
N, K = map(int, sys.stdin.readline().split())


print(int(fac(N)/(fac(K)*fac(N-K))))
