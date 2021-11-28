import sys

def roomNum():
    N = int(sys.stdin.readline().split()[0])
    i = 0
    while True:
        if i == 0:
            if N == 1:
                return 1
            i += 1
            continue
        max_ = 1 + 6*((i)*(i+1)//2)
        min_ = max_ - 6*i
        if N >= min_ and N <= max_:
            return i + 1
        i += 1
print(roomNum())