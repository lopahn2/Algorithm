import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    temp = [a, b, c]
    hypotenuse = max(a,b,c)
    container = 0
    for num in temp:
        if num == hypotenuse:
            continue
        container += num ** 2
    if container == 0:
        break
    if hypotenuse ** 2 == container:
        print("right")
    else:
        print("wrong")
    