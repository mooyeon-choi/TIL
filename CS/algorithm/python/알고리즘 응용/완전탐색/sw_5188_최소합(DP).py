t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not i and not j:
                continue
            elif not i and j:
                board[i][j] = board[i][j - 1] + board[i][j]
            elif not j and i:
                board[i][j] = board[i-1][j] + board[i][j]
            else:
                board[i][j] = min(board[i-1][j], board[i][j-1]) + board[i][j]
    print('#{} {}'.format(tc, board[n-1][n-1]))