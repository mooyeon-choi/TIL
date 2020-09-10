from collections import deque


def BFS(i, j):
    global answer
    q = deque([])
    q.append((i, j))
    miro[i][j] = 1
    while q:
        u, v = q.popleft()
        if miro[u][v] == '2':
            answer = 1
            return
        for a in range(4):
            if -1 < u + x[a] < n and -1 < v + y[a] < n:
                if miro[u + x[a]][v + y[a]] == '0' or miro[u + x[a]][v + y[a]] == '2':
                    miro[u + x[a]][v + y[a]] = 1
                    q.append((u + x[a], v + y[a]))


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n = int(input())
    m = [input() for _ in range(n)]
    miro = []
    for number in m:
        miro.append(list(number))
    for i in range(n):
        for j in range(n):
            if miro[i][j] == '3':
                BFS(i, j)
    print('#{} {}'.format(tc, answer))