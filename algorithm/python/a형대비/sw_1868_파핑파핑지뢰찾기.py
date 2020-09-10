from collections import deque

find = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def BFS(i, j):
    que = deque()
    que.append((i, j))
    while que:
        u, v = que.popleft()
        count = 0
        for k in range(8):
            if 0 <= u + find[k][0] < n and 0 <= v + find[k][1] < n:
                if board[u + find[k][0]][v + find[k][1]] == '*':
                    count += 1
        if not count:
            for k in range(8):
                if 0 <= u + find[k][0] < n and 0 <= v + find[k][1] < n:
                    if board[u + find[k][0]][v + find[k][1]] == '.':
                        board[u + find[k][0]][v + find[k][1]] = 0
                        que.append((u + find[k][0], v + find[k][1]))
        board[u][v] = count

for tc in range(1, int(input()) + 1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                for k in range(8):
                    if 0 <= i+find[k][0] < n and 0 <= j+find[k][1] < n:
                        if board[i+find[k][0]][j+find[k][1]] == '*':
                            break
                else:
                    answer += 1
                    BFS(i, j)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                answer += 1
    print('#{} {}'.format(tc, answer))