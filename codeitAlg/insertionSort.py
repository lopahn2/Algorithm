def insertionSort(list_):
    for i in range(1,len(list_)):
        for idx in range(0,i):
            if list_[idx] > list_[i]:
                list_[idx], list_[i] = list_[i], list_[idx]
    
    return list_
                
    
    
print(insertionSort([3,6,1,5,2,4]))