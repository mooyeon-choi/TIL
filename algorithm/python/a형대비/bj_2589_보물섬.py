from collections import deque


def bfs(i, j):
    global max_num, count
    deq = deque()
    deq.append((i, j))
    visit[i][j] = 1
    count = 0
    while deq:
        for l in range(len(deq)):
            u, v = deq.popleft()
            for dirc in range(4):
                if 0 <= u + x[dirc] < h and 0 <= v + y[dirc] < w:
                    if not visit[u + x[dirc]][v + y[dirc]] and trs[u + x[dirc]][v + y[dirc]] == 'L':
                        visit[u + x[dirc]][v + y[dirc]] = 1
                        deq.append((u + x[dirc], v + y[dirc]))
        count += 1
    if count > max_num:
        max_num = count - 1


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
count = 0
h, w = map(int, input().split())
trs = [list(input()) for _ in range(h)]
max_num = 0
for i in range(h):
    for j in range(w):
        visit = [[0]*w for _ in range(h)]
        if trs[i][j] == 'L':
            bfs(i, j)
print(max_num)