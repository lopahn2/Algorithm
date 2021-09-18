import sys

string_ = sys.stdin.readline().split()[0].upper()



alpha = {}

for i in range(len(string_)):
    try : alpha[string_[i]] += 1
    except : alpha[string_[i]] = 1

# 해당 값이 있으면! 객체의 값 추가하기
# 없으면 에러가 발생되므로 except로 초기화 해주기

answer = [k for k, v in alpha.items() if v == max(alpha.values())]
# 리스트에 바로 for문으로 값 넣어주기

if len(answer) != 1:
    print("?")
else:
    print(answer[0])