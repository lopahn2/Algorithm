import sys
N = int(sys.stdin.readline().split()[0])
_string = sys.stdin.readline().split()[0]
_sum = 0
for i in range(N):
    _sum += int(_string[i])
    
print(_sum)

    
