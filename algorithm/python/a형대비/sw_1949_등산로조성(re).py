def DFS(i, j, k, now, cnt):
    global answer
    if cnt > answer:
        answer = cnt
    for v in range(4):
        if 0 <= i+x[v] < n and 0 <= j+y[v] < n:
            if not visit[i+x[v]][j+y[v]]:
                if board[i+x[v]][j+y[v]] < now:
                    visit[i + x[v]][j + y[v]] = 1
                    DFS(i+x[v], j+y[v], k, board[i+x[v]][j+y[v]], cnt + 1)
                    visit[i + x[v]][j + y[v]] = 0
                elif board[i+x[v]][j+y[v]] < now + k:
                    visit[i + x[v]][j + y[v]] = 1
                    DFS(i + x[v], j + y[v], 0, now - 1, cnt + 1)
                    visit[i + x[v]][j + y[v]] = 0

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    answer = 0
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_num = max(list(map(lambda num: max(num), board)))
    for i in range(n):
        for j in range(n):
            visit = [[0]*n for _ in range(n)]
            if board[i][j] == max_num:
                visit[i][j] = 1
                DFS(i, j, k, board[i][j], 1)
    print('#{} {}'.format(tc, answer))