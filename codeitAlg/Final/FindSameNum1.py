def find_same_number(some_list):
    container = {}
    
    for ele in some_list:
        
        if ele in container:
            return ele
        container[ele] = True
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
