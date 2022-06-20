N = int(input())
members = []
for i in range(N):
    x, y = map(int, input().split())
    members.append((x, y))
tier = [1 for i in range(N)]
for i in range(N):
    for j in range(N):
        if j == i :
            continue
        if members[i][0] < members[j][0] and members[i][1] < members[j][1]:
            tier[i] += 1
print(' '.join(map(str,tier)))