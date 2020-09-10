from collections import deque

def bfs(i, j):
    que = deque([i, j])
    while que:
        u, v = que.popleft()
        if not removed[u][(circles[u][0] + j) % m + 1]:
            removed[i][(circles[i][0] + j) % m + 1] = 1
            for z in range(4):
                if 0 < i + dirs[z][0] <= n and 0 <= j + dirs[z][1] < m:
                    if not removed[i + dirs[z][0]][(circles[i + dirs[z][0]][0] + j + dirs[z][1]) % m + 1]:
                        if circles[i + dirs[z][0]][(circles[i + dirs[z][0]][0] + j + dirs[z][1]) % m + 1] == circles[i][
                            (circles[i][0] + j) % m + 1]:


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m, t = map(int, input().split())
circles = [0] + [[0] + list(map(int, input().split())) for _ in range(n)]
answer = 0
removed = [[0]*(m+1) for _ in range(n+1)]
for _ in range(t):
    x, d, k = map(int, input().split())
    count = 1
    total = 0
    while x * count <= n:
        if d:
            circles[x*count][0] += k
        else:
            circles[x*count][0] -= k
        count += 1
    for i in range(1, n + 1):
        for j in range(m):
            count = 0
            if not removed[i][(circles[i][0] + j) % m + 1]:
                for z in range(4):
                    if 0 < i + dirs[z][0] <= n and 0 <= j + dirs[z][1] < m:
                        if not removed[i + dirs[z][0]][(circles[i + dirs[z][0]][0] + j + dirs[z][1]) % m + 1]:
                            if circles[i + dirs[z][0]][(circles[i + dirs[z][0]][0] + j + dirs[z][1]) % m + 1] == circles[i][(circles[i][0] + j) % m + 1]:
                                removed[i + dirs[z][0]][(circles[i + dirs[z][0]][0] + j + dirs[z][1]) % m + 1] = 1
                                count += 1
            if count > 0:
                total += 1
                removed[i][(circles[i][0] + j) % m + 1] = 1
    if not total:
        numsum = 0
        cnt = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not removed[i][j]:
                    numsum += circles[i][j]
                    cnt += 1
        avg = numsum / cnt
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not removed[i][j]:
                    if circles[i][j] < avg:
                        circles[i][j] += 1
                    elif circles[i][j] > avg:
                        circles[i][j] -= 1


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not removed[i][j]:
            answer += circles[i][j]

print(answer)