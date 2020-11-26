from collections import deque

for tc in range(1, int(input()) + 1):
    n = int(input())
    m = int(input())
    up = [[] for _ in range(n+1)]
    down = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        up[u].append(v)
        down[v].append(u)
    