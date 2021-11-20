def staircase(stairs, possible_steps):
    container = [1,1]
    for height in range(2, stairs + 1):
        container.append(0)
        
        for stair in possible_steps:
            if height - stair >= 0:
                container[height] += container[height-stair]
    return container[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))