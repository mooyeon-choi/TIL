import sys
sys.setrecursionlimit(100000)

def spin(xi, di, ki):
    if not di:
        for i in range(xi, N+1, xi):
            board[i] = board[i][-ki:] + board[i][:-ki]
    else:
        for i in range(xi, N+1, xi):
            board[i] = board[i][ki:] + board[i][:ki]


def DFS(x, y, num):
    count = 0
    for i in range(4):
        if 0 < x + dirs[i][0] <= N:
            if board[x + dirs[i][0]][(y + dirs[i][1]) % M] == num:
                board[x + dirs[i][0]][(y + dirs[i][1]) % M] = 0
                board[x][y] = 0
                DFS(x + dirs[i][0], (y + dirs[i][1]) % M, num)
                count += 1
    if count:
        return 1
    else:
        return 0


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M, T = map(int, input().split())

board = [[0]] + [list(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    X, D, K = map(int, input().split())
    spin(X, D, K)
    cnt = 0
    for i in range(1, N + 1):
        for j in range(M):
            if board[i][j]:
                cnt += DFS(i, j, board[i][j])
    if not cnt:
        numsum = 0
        numcnt = 0
        for i in range(1, N + 1):
            for j in range(M):
                if board[i][j]:
                    numsum += board[i][j]
                    numcnt += 1
        if not cnt:
            numsum = 0
            numcnt = 0
            for i in range(1, N + 1):
                for j in range(M):
                    if board[i][j]:
                        numsum += board[i][j]
                        numcnt += 1
            if numcnt:
                numsum /= numcnt
                for i in range(1, N + 1):
                    for j in range(M):
                        if board[i][j]:
                            if board[i][j] < numsum:
                                board[i][j] += 1
                            elif board[i][j] > numsum:
                                board[i][j] -= 1
answer = 0
for i in range(N+1):
    answer += sum(board[i])
print(answer)