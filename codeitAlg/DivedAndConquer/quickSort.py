def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1] 
    


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    p = end

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
    swap_elements(my_list, b, p)
    p = b

    # pivot의 최종 인덱스를 리턴해 준다
    return p

    
# 퀵 정렬
def quicksort(my_list, start, end):
    # 코드를 작성하세요.
    if end - start < 1:
        return
    
    p = partition(my_list, start, end)
    quicksort(my_list, start, p-1)
    quicksort(my_list, p+1, end)

    # start와 end를 쓰지 않고 사용하기.
# def quicksort(my_list, start = 0 , end = None):
#     # 이전 과제에서 작성한 코드를 붙여 넣으세요!
#     if end == None:
#         end = len(my_list) - 1
#     if end - start < 1:
#         return
    
#     p = partition(my_list, start, end)
#     quicksort(my_list, start, p-1)
#     quicksort(my_list, p+1, end)
    
    
    
# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)