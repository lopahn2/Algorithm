def max_crossing_sum(profits, start, end):
    mid = (start + end)//2
    leftCount = 0
    leftMax = profits[mid]
    
    for i in range(mid, start-1, -1):
        leftCount += profits[i]
        leftMax = max(leftCount, leftMax)
        
    
    rightCount = 0
    rightMax = profits[mid+1]
    
    for i in range(mid+1, end):
        rightCount += profits[i]
        rightMax = max(rightMax, rightCount)
    
    return rightMax + leftMax
        


def sublist_max(profits, start, end):
    if start == end:
        return profits[start]
    
    mid = (start+end)//2
    
    leftMax = sublist_max(profits, start, mid)
    rightMax = sublist_max(profits, mid+1, end)
    centerMax = max_crossing_sum(profits, start, end)
    
    return(max(leftMax, rightMax, centerMax))

    
    
    
    
    
    
    
# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))