import collections as col

def BFS(i, j):
    que = col.deque()
    que.append((i, j))
    while que:
        u, v = que.popleft()
        island[u][v] = cnt
        for k in range(4):
            if 0 <= u + dirs[k][0] < N and 0 <= v + dirs[k][1] < M:
                if board[u + dirs[k][0]][v + dirs[k][1]] and not island[u + dirs[k][0]][v + dirs[k][1]]:
                    que.append((u + dirs[k][0], v + dirs[k][1]))


def cal_len():
    global num
    for i in range(N):
        cnt = 0
        num = island[i][0]
        for j in range(M):
            if not island[i][j]:
                cnt += 1
            else:
                cal_num(cnt, i, j)
                cnt = 0

    for j in range(M):
        cnt = 0
        num = island[0][j]
        for i in range(N):
            if not island[i][j]:
                cnt += 1
            else:
                cal_num(cnt, i, j)
                cnt = 0

def cal_num(cnt, i, j):
    global num
    if not num:
        num = island[i][j]
    elif num != island[i][j]:
        if tuple(sorted([num, island[i][j]])) not in connect_len and cnt > 1:
            connect_len[tuple(sorted([num, island[i][j]]))] = cnt
        elif cnt > 1 and connect_len[tuple(sorted([num, island[i][j]]))] > cnt:
            connect_len[tuple(sorted([num, island[i][j]]))] = cnt
        num = island[i][j]


def sorting():
    for key, value in connect_len.items():
        sorted_value.append((key[0], key[1], value))

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
connect_len = {}
island = [[0]*M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] and not island[i][j]:
            cnt += 1
            BFS(i, j)



cal_len()
sorted_value = []
sorting()
result = [1] + [0]*(cnt)
answer = -1
if sorted_value:
    sorted_value.sort(key=lambda x: x[2])
    numsum = sorted_value[0][2]
    result[sorted_value[0][0]], result[sorted_value[0][1]] = 1, 1
    for i in range(cnt - 2):
        for j in range(1, len(sorted_value)):
            if result[sorted_value[j][0]] and not result[sorted_value[j][1]]:
                result[sorted_value[j][1]] = 1
                numsum += sorted_value[j][2]
                break
            if result[sorted_value[j][1]] and not result[sorted_value[j][0]]:
                result[sorted_value[j][0]] = 1
                numsum += sorted_value[j][2]
                break
        else:
            break
    else:
        answer = numsum

print(answer)
