def fact(n): # n = 문제를 식별하는 값, 문제의 크기,
    if n == 0 or 1:
        return 1

    return fact(n-1) * n