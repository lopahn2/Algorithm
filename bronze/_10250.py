import sys

T = int(sys.stdin.readline().split()[0])

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    roomNum = N//H + 1
    floor = N % H
    if floor == 0:
        roomNum = N//H
        floor = H
    print(f'{floor*100 + roomNum}')
        
# t = int(input())

# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n//h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n//h
#         floor = h
#     print(f'{floor*100+num}')