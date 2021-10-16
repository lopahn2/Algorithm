def consecutive_sum(start, end):
    container = [x for x in range(start, end+1)]
    midIdx = len(container) // 2
    if len(container) == 1:
        return container[0]
    
    return consecutive_sum(container[0], container[midIdx-1]) + consecutive_sum(container[midIdx], container[len(container)-1])
        

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))