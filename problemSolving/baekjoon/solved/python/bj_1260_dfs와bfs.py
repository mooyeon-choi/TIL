from collections import deque


def dfs(v):
    for i in G[v]:
        if not visit[i]:
            visit[i] = 1
            result_d.append(i)
            dfs(i)


def bfs(v):
    visit[v] = 1
    deq = deque()
    deq.append(v)
    while deq:
        num = deq.popleft()
        result_b.append(num)
        for number in G[num]:
            if not visit[number]:
                visit[number] = 1
                deq.append(number)


n, m, v = map(int, input().split())
G = [[] for _ in range(n + 1)]
result_d = []
result_b = []
for _ in range(m):
    u, w = map(int, input().split())
    G[u] += [w]
    G[w] += [u]
for i in range(n + 1):
    G[i].sort()
visit = [0]*(n+1)
visit[v] = 1
result_d.append(v)
dfs(v)
visit = [0]*(n+1)
bfs(v)
print(*result_d)
print(*result_b)