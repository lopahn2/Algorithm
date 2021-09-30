import sys

n = int(sys.stdin.readline().split()[0])

answer = []

for i in range(n):
    prob = sys.stdin.readline().split()[0]
    ans = 0
    circle_num = 0

    for j in range(len(prob)):
        if prob[j] == "O":
            circle_num += 1
            ans += circle_num
            
        else:
            circle_num = 0
            
                
    answer.append(ans)
    ans = 0

for i in range(len(answer)):
    print(answer[i])
