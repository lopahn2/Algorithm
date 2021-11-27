import sys

T = int(sys.stdin.readline().split()[0])

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    roomNum = N//H
    if roomNum == 0:
        print(str(N) + "01")
    else:
        if N%H == 0:
            print(str(H)+"0"+str(roomNum))
        else:
            print(str(N%H)+"0"+str(roomNum+1))
# t = int(input())

# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n//h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n//h
#         floor = h
#     print(f'{floor*100+num}')