# 재귀적으로 문제를 푸는 것
# = 부분 문제의 답을 이용해서 기존 문제를 푸는 것.

def countdonw(n):
    if n>0:
        print(n)
        countdonw(n-1)


countdonw(4)

def factorial(n):
    if n == 0: # base case
        return 1
    if n > 0: # recursive case
        return factorial(n-1) * n

print(factorial(4))
    
# call stack이 너무 쌓이는 거 같을 때 반복문을 사용.