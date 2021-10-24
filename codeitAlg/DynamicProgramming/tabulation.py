def fib_tab(n):
    # 코드를 작성하세요.
    cache = [1,1]
    for i in range(2,n):
        cache.append(cache[i-1] + cache[i-2])
    return cache[n-1]
# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))