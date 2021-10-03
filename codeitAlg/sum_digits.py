# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    lens = len(str(n))-1
    if lens == 0:
        return n 
    return n // (10 ** lens) + sum_digits(n % (10 ** (lens)))
    

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))