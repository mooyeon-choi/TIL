def DFS(v):
    if cant[v] == 0:
        visit[v] = 1;
        print(v, end=' ')
    else:
        return
    if G[v]:
        for w in G[v]:
            if not visit[w]:
                cant[w] -= 1
                DFS(w)

for tc in range(1, 11):
    V, E = map(int, input().split())  # 정점수, 간선수
    num_list = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]  # 1 ~ v 까지
    U = [[] for _ in range(V + 1)]  # 1 ~ v 까지
    visit = [0] * (V + 1)
    cant = [0] * (V + 1)
    for i in range(E):
        G[num_list[2 * i]].append(num_list[2 * i + 1])
        U[num_list[2 * i + 1]].append(num_list[2 * i])
        cant[num_list[2 * i + 1]] += 1
    print('#{}'.format(tc), end=' ')
    for i in range(1, V + 1):
        if cant[i] == 0:
            DFS(i)
    print('')