import sys

number = map(int, sys.stdin.readline().split())

target = 0
for i in number:
    target += i**2

    
print(target%10)