import sys
N = int(sys.stdin.readline().split()[0])

for i in range(N):
    print(" "*(N-i-1) + "*"*(i+1))