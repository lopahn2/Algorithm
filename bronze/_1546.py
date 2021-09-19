import sys

Numbers = int(sys.stdin.readline().split()[0])
oldScore = list(map(int,sys.stdin.readline().split()))
maxScore = max(oldScore)

oldScore = [x/maxScore * 100 for x in oldScore]
print(sum(oldScore)/Numbers)
 