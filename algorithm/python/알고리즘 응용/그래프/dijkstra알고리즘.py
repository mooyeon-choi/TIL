from collections import deque
def BFS(s):
    D = [0xffffff] * (V + 1)
    visit = [False] * (V + 1)
    D[s] = 0
    Q.append(s); D[s] = 0

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if D[v] > D[u] + w:
                D[v] += D[u] + w
                Q.append(v)
