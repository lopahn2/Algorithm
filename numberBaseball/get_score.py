def get_score(guess, solution):
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