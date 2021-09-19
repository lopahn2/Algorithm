from random import randint


def generate_numbers():
    # 지난 과제의 코드를 붙여 넣으세요.
    numbers = []
    while len(numbers) < 3:
        num = randint(0,9)
        if num not in numbers:
            numbers.append(num)
        else:
            continue
    
    # 코드를 작성하세요.

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        num = int(input(f"{len(new_guess)+1}번째 숫자를 입력하세요:"))
        if (num < 0) or (num < 0):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            num = int(input(f"{len(new_guess)+1}번째 숫자를 입력하세요:"))
        if num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        new_guess.append(num)    
    
    return new_guess

def get_score(guess, solution):
    # 지난 과제의 코드를 붙여 넣으세요.
    strike_count = 0
    ball_count = 0
    for num in guess:
        if num in solution:
            if guess.index(num) == solution.index(num):
                strike_count += 1
            else:
                ball_count += 1
    # 코드를 작성하세요.

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.
while True:
    new_guess = take_guess()
    strike_count, ball_count = get_score(new_guess, ANSWER)
    print(f"{strike_count}S {ball_count}B")
    if strike_count == 3:
        break
    tries +=1
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
