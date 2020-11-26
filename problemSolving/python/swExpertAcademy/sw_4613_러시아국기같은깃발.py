t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    background = [list(input()) for _ in range(n)]
    answer = 0xffffff
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                num = count(i, j, k)
                if num < answer:
                    answer = num
    print('#{} {}'.format(tc, answer))