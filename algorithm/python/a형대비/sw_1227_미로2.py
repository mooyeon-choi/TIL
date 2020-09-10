from collections import deque

def bfs(i, j):
    que = deque()
    que.append((i, j))
    while que:
        u, v = que.popleft()
        miro[u][v] = 1
        for k in range(4):
            if 0 <= u + x[k] < 100 and 0 <= v + y[k] < 100:
                if not miro[u + x[k]][v + y[k]]:
                    que.append((u + x[k], v + y[k]))
                elif miro[u + x[k]][v + y[k]] == 3:
                    return 1
    return 0


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
for _ in range(10):
    tc = int(input())
    miro = [list(map(int, list(input()))) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if miro[i][j] == 2:
                answer = bfs(i, j)
    print('#{} {}'.format(tc, answer))