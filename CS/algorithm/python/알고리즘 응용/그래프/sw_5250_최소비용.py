for tc in range(1, int(input()) + 1):
    n = int(input())
    background = [list(map(int, input().split())) for _ in range(n)]

    print('#{} {}'.format(tc, memo[n-1][n-1]))