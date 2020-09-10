import sys; sys.stdin = open('DFS_input.txt', 'r')

def DFS(v):
    visit[v] = True; print(v, end=' ')

    for w in G[v]:
        if not visit[w]:
            DFS[w]
            
V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V + 1)]   # 1 ~ v 까지
visit = [False] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V + 1):
    print(i, '-->', G[i])