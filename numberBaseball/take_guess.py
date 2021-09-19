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

print(take_guess())