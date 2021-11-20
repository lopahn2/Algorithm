def max_profit(stock_list):
    max_profit_so_far = stock_list[1] - stock_list[0]
    
    for i in range(len(stock_list)):
        for j in range(i+1,len(stock_list)):
            max_profit_so_far = max(max_profit_so_far, stock_list[j] - stock_list[i])
    return max_profit_so_far
# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))