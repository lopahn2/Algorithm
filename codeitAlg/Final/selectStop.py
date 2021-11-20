def select_stops(water_stops, capacity):
    # 코드를 작성하세요. 
    MaxCapacity = capacity
    capacity -= water_stops[0]
    container = []
    for i in range(1, len(water_stops)):
        diff = water_stops[i] - water_stops[i-1]
        if capacity >= diff:
            capacity -= diff
            
        else:
            container.append(water_stops[i-1])
            capacity = MaxCapacity - diff
    return container + [water_stops[-1]]
    
    

    
# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))