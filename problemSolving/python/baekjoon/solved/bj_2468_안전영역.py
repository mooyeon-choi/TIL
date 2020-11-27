from collections import deque

def bfs(i, j):
    result = deque()
    result.append((i, j))
    visit[i][j] = k
    while result:
        for _ in range(len(result)):
            u, v = result.popleft()
            for a in range(4):
                if 0 <= u+x[a] < n and 0 <= v+y[a] < n:
                    if island[u+x[a]][v+y[a]] > k and not visit[u+x[a]][v+y[a]]:
                        visit[u + x[a]][v + y[a]] = 1
                        result.append((u+x[a], v+y[a]))

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]
answer = 0
count = 1
k = 0
while count:
    count = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if island[i][j] > k and not visit[i][j]:
                bfs(i, j)
                count += 1
    if count > answer:
        answer = count
    k += 1
print(answer)