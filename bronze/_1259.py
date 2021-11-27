import sys

while True:
    target = sys.stdin.readline().split()[0]
    if target == "0":
        break
    lens = len(target)
    midLen = lens // 2
    flag = True
    
    for i in range(midLen):
        if target[i] == target[lens-1-i]:
            continue
        else:
            flag = False
    if flag == True:
        print("yes")
    else:
        print("no")
    
    
    
    