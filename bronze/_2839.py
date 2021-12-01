import sys

N = int(sys.stdin.readline().split()[0])

ans = []

for i in range(1 + (N//5)):
    three = (N - 5*i) // 3
    remain = N - (5*i + 3*three)
    if remain == 0:
        ans.append(three + i)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
    

