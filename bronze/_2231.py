import sys

def findN():
    N = sys.stdin.readline().split()[0]
    
    for num in range(int(N)):
        temp = 0
        remain = int(N) - num
        Num = str(num)
        for n in range(len(Num)):
            temp += int(Num[n])
        if remain == temp:
            return num
    return 0    

print(findN())
    