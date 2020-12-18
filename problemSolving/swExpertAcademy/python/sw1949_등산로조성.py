def DFS(i, j, k, now, cnt):
    global answer
    if answer < cnt:
        answer = cnt
    for d in range(4):
        if 0 <= i + dirs[d][0] < N and 0 <= j + dirs[d][1] < N and not visit[i + dirs[d][0]][j + dirs[d][1]]:
            if now > board[i + dirs[d][0]][j + dirs[d][1]]:
                visit[i + dirs[d][0]][j + dirs[d][1]] = 1
                DFS(i + dirs[d][0], j + dirs[d][1], k, board[i + dirs[d][0]][j + dirs[d][1]], cnt + 1)
                visit[i + dirs[d][0]][j + dirs[d][1]] = 0
            elif now + k > board[i + dirs[d][0]][j + dirs[d][1]]:
                visit[i + dirs[d][0]][j + dirs[d][1]] = 1
                DFS(i + dirs[d][0], j + dirs[d][1], 0, board[i][j] - 1, cnt + 1)
                visit[i + dirs[d][0]][j + dirs[d][1]] = 0


dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for tc in range(1, int(input()) + 1):
    answer = 0
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    top = max(map(lambda x: max(x), board))
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == top:
                visit[i][j] = 1
                DFS(i, j, K, top, 1)
                visit[i][j] = 0
    print(f'#{tc} {answer}')