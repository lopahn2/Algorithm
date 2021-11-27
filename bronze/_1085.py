import sys

line = sys.stdin.readline().split()

w = int(line[2])
h = int(line[3])
x = int(line[0])
y = int(line[1])

print(min(w-x,h-y,x,y))