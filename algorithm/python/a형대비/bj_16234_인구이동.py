import sys
from collections import deque

I = sys.stdin.readline

def bfs(i, j):
    visit[i][j] = count
    cnt = 0
    deq = deque()
    deq.append((i, j))
    n_list.append((i, j))
    while deq:
        u, v = deq.popleft()
        for k in range(4):
            if 0 <= u+x[k] < n and 0 <= v+y[k] < n:
                if not visit[u+x[k]][v+y[k]] and l <= abs(country[u+x[k]][v+y[k]] - country[u][v]) <= r:
                    visit[u+x[k]][v+y[k]] = count
                    deq.append((u+x[k], v+y[k]))
                    n_list.append((u+x[k], v+y[k]))
                    cnt += 1
    if cnt == 0:
        visit[i][j] = 0
        n_list.pop()
    return cnt


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
n, l, r = map(int, I().split())
country = [list(map(int, I().split())) for _ in range(n)]

answer = 0
roof = 1
while roof:
    roof = 0
    visit = [[0]*n for _ in range(n)]
    count = 1
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                result = []
                n_list = []
                number = bfs(i, j)
                if number > 0:
                    roof += 1
                    count += 1
                for u, v in n_list:
                    result.append(country[u][v])
                for u, v in n_list:
                    country[u][v] = sum(result)//len(result)
    for i in range(len(country)):
        print(country[i])
    print('-----------------------------------')
    answer += 1
print(answer - 1)