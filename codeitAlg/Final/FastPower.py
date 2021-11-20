def power(x, y):
    if y == 0:
        return 1
    
    if y % 2 == 0:
        return power(x, y//2)*power(x,y//2)
    else:
        return power(x,y//2)*power(x,y//2)*x

    
    
    
# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))