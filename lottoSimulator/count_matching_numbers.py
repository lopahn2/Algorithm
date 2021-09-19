def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count

# 두 리스트 사이 같은 값의 개수 찾기!