def dfs(num):
    visit[num] = 1
    for i in G[num]:
        if not visit[i]:
            dfs(i)


n = int(input())
m = int(input())
G = [[] for _ in range(n + 1)]
visit = [0]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
dfs(1)
print(sum(visit) - 1)