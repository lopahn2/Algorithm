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
    
print(generate_numbers(6))