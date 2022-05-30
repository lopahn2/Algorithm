A, B = map(int, input().split())

def f(n, x):
    for i in range(1, n+1):
        if x == 0:
            return 1
        if (i*(i-1) / 2) <= x < (i*(i+1) / 2):
            return i
sum = 0
for i in range(A-1, B):
    sum += f(1000,i)
print(sum)
