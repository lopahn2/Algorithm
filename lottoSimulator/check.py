from count_matching_numbers import count_matching_numbers

def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    count = count_matching_numbers(numbers, winning_numbers)
    
    if count == 6:
        if winning_numbers[6] in numbers:
            return (50000000)
        else:
            return (1000000000)
    elif count == 5:
        if winning_numbers[6] in numbers:
            return (50000000)
        else:
            return (1000000)
    elif count == 4:
        if winning_numbers[6] in numbers:
            return (5000)
        else:
            return (50000)
    elif count == 3:
        if winning_numbers[6] in numbers:
            return()
        else:
            return(5000)
    else:
        return()
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))