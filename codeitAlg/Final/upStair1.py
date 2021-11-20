def staircase(n):
    # 코드를 작성하세요.
    temp1, temp2 = 1, 1
    for i in range(n):
        temp1, temp2 = temp2, temp1+temp2
    return temp1

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
