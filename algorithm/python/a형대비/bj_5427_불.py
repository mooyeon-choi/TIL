from collections import deque

def fire():
    deq = deque()
    for i in range(h):
        for j in range(w):
            if room[i][j] == '*':
                deq.append((i, j))
                burn[i][j] = 1
    while deq:
        u, v = deq.popleft()
        for k in range(4):
            if 0 <= u+x[k] < h and 0 <= v+y[k] < w:
                if room[u+x[k]][v+y[k]] != '#' and burn[u+x[k]][v+y[k]] == 10000:
                    burn[u+x[k]][v+y[k]] = burn[u][v] + 1
                    deq.append((u+x[k], v+y[k]))

def esc():
    count = 0
    deq = deque()
    for i in range(h):
        for j in range(w):
            if room[i][j] == '@':
                deq.append((i, j))
    while deq:
        count += 1
        for _ in range(len(deq)):
            u, v = deq.popleft()
            if u == 0 or u == h-1 or v == 0 or v == w-1:
                if burn[u][v] > count:
                    return count
            for k in range(4):
                if 0 <= u+x[k] < h and 0 <= v+y[k] < w:
                    if room[u+x[k]][v+y[k]] == '.':
                        room[u + x[k]][v + y[k]] = '@'
                        deq.append((u+x[k], v+y[k]))
    return 'IMPOSSIBLE'

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    room = [list(input()) for _ in range(h)]
    burn = [[10000]*w for _ in range(h)]
    fire()
    print(esc())