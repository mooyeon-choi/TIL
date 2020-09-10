from collections import deque
def BFS(s):
    D = [0] * (V + 1)
    visit = [False] * (V + 1)
    Q = deque()
    Q.append(s); D[s] = 0

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if D[v] > D[u] + w:
                D[v] += D[u] + w
                Q.append(v)
