from collections import deque

while True:
    s = input()
    if s == ".":
        break
    queue = deque()
    temp = True
    for ss in s:
        if ss == "(" or ss == "[":
            queue.append(ss)
        elif ss == ")":
            if len(queue) == 0 or queue[-1] == "[":
                temp = False
                break
            elif queue[-1] == "(":
                queue.pop()
        elif ss == "]":
            if len(queue) == 0 or queue[-1] == "(":
                temp = False
                break
            elif queue[-1] == "[":
                queue.pop()

    if len(queue) == 0 and temp:
        print("yes")
    else:
        print("no")
        

