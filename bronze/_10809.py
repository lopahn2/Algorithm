import sys

s = sys.stdin.readline().split()[0]
alphabet = "abcdefghijklmnopqrstuvwxyz"
ans = []


for i in range(len(alphabet)):
    ans.append(-1)

for i in range(len(s)):
    if s[i] in alphabet:
        if ans[alphabet.index(s[i])] == -1:
            ans[alphabet.index(s[i])] = i
        


for i in range(len(ans)):
    print(ans[i], end=" ")