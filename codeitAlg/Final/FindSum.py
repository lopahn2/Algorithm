def sum_in_list(search_sum, sorted_list):
    left = 0
    right = len(sorted_list)-1
    
    for i in range(len(sorted_list)):
        if sorted_list[right] + sorted_list[left] == search_sum:
            return True
        elif sorted_list[right] + sorted_list[left] > search_sum:
            right -=1
        else:
            left += 1
    return False
    
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))