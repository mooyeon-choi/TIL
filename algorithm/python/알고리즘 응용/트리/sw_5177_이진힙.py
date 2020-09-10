t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    result = [0]*(n+1)
    for i in range(1, n + 1):
        result[i] = numbers[i]
        if i > 1:
            while i:
                if result[i] < result[i//2]:
                    result[i], result[i//2] = result[i//2], result[i]
                i //= 2
    while n:
        n //= 2
        answer += result[n]

    print('#{} {}'.format(tc, answer))