def trapping_rain(buildings):
    container = 0
    left = []
    right = []
    
    for i in range(len(buildings)):
        left.append(max(buildings[:i+1]))
        right.append(max(buildings[i:]))
        
    for i in range(len(buildings)):
        container += (min(left[i], right[i]) - buildings[i])
    return container

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))