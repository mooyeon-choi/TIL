from collections import deque

def bfs(i, j):
    global max_i, max_j, count
    count += 1
    matrix = deque()
    matrix.append((i, j))
    while matrix:
        u, v = matrix.popleft()
        mat[u][v] = 0
        if u > max_i:
            max_i = u
        if v > max_j:
            max_j = v
        for k in range(4):
            if 0 <= u+x[k] < n and 0 <= v+y[k] < n:
                if mat[u + x[k]][v + y[k]]:
                    mat[u + x[k]][v + y[k]] = 0
                    matrix.append((u+x[k], v+y[k]))


y = [0, 1, 0, -1]
x = [-1, 0, 1, 0]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    result = []
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                max_i = max_j = 0
                bfs(i, j)
                if not result:
                    result = [((max_i - i + 1) * (max_j - j + 1), max_i - i + 1, max_j - j + 1)]
                else:
                    result += [((max_i - i + 1) * (max_j - j + 1), max_i - i + 1, max_j - j + 1)]
    result.sort()
    answer = [count]
    for re in result:
        answer.append(re[1])
        answer.append(re[2])
    print('#{}'.format(tc), *answer)