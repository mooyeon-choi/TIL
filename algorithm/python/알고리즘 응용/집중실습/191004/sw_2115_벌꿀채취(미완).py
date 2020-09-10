t = int(input())
for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    memo = [[0]*(n - m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n - m + 1):
            maxsum = 0
            for x in range(1 << m):
                numsum = []
                num = 0
                for y in range(m):
                    if x & (1<<y):
                        numsum.append(board[i][j+y])
                if sum(numsum) <= c:
                    for number in numsum:
                        num += number**2
                    if num > maxsum:
                        maxsum = num
            memo[i][j] = maxsum
    maxvalue = max(memo)
    print(maxvalue)
