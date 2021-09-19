from random import randint


def generate_numbers(n):
    # 코드를 작성하세요.
    _list = []
    while n > 0:
        num = randint(1,45)
        if num in _list:
            continue
        else:
            _list.append(num)
        n -= 1
    return _list


def draw_winning_numbers():
    # 코드를 작성하세요.
    sorted_list = sorted(generate_numbers(6))
    while True:
        num = randint(1,45)
        if num in sorted_list:
            continue
        else:
            sorted_list.append(num)
            break
    return sorted_list


def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count

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
            return(0)
        else:
            return(5000)
    else:
        return(0)
    
