def sublist_max(profits):
    # 코드를 작성하세요.
    container = []
    for i in range(len(profits)):
        if profits[i] > 0:
            container.append(i) 
    return sum(profits[container[0]:container[-1]+1])

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))