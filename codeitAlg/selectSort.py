def selectSort(list_):

    for i in range(len(list_)):
        minIndex = i
        for j in range(i+1,len(list_)):
            if list_[i] < list_[j]:
                continue
            elif list_[i] > list_[j]:
                minIndex = j
        temp = list_[i]        
        list_[i] = list_[minIndex]
        list_[minIndex] = temp
    return list_
            
print(selectSort([1,4,3,2,1]))            
            
