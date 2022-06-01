import sys
N = int(sys.stdin.readline())
unsortedList = []
for i in range(N):
    unsortedList.append(int(sys.stdin.readline()))

for num in sorted(unsortedList):
    print(num)

