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
        
        
print(draw_winning_numbers())