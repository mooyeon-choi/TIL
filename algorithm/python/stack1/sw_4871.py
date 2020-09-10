def DFS(v):
    visit[v] = True;
    for w in G[v]:
        if not visit[w]:
            DFS(w)

t = int(input())

for tc in range(1, t + 1):
    V, E = map(int, input().split())  # 정점수, 간선수
    G = [[] for _ in range(V + 1)]  # 1 ~ v 까지
    visit = [False] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    print(G)
    start, end = map(int, input().split())

    DFS(start)
    if visit[end] == 1:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(tc, result))