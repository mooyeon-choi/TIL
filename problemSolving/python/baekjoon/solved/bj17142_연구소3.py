import collections as col

# 부분집합 찾기
def DFS(cnt, idx_list):
    if len(idx_list) == M:
        subset.append(idx_list)
        return
    for i in range(cnt, total_virus):
        if not used[i]:
            used[i] = 1
            DFS(i, idx_list + [i])
            used[i] = 0

# 각 위치에서 BFS
def BFS(i, j, idx):
    que = col.deque()
    que.append((i, j))
    cnt = 1
    while que:
        for _ in range(len(que)):
            u, v = que.popleft()
            for n in range(4):
                if 0 <= u + dirs[n][0] < N and 0 <= v + dirs[n][1] < N:
                    if board[u + dirs[n][0]][v + dirs[n][1]] != 1:
                        if void_dict[(u + dirs[n][0], v + dirs[n][1])][idx] == 9999:
                            void_dict[(u + dirs[n][0], v + dirs[n][1])][idx] = cnt
                            que.append((u + dirs[n][0], v + dirs[n][1]))
        cnt += 1


# M개씩 뽑아서 비교해보며 가장 큰 수 찾기
def find_num(idxs):
    global answer
    max_value = 0
    for numbers in results:
        min_value = 9999
        for idx in idxs:
            if numbers[idx] < min_value:
                min_value = numbers[idx]
        if min_value > max_value:
            max_value = min_value
        if max_value >= answer:
            return
    answer = max_value


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total_virus = 0
void_dict = {}
subset = []
answer = 9999

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            total_virus += 1
            void_dict[(i, j)] = [9999] * 10
        elif not board[i][j]:
            void_dict[(i, j)] = [9999]*10

used = [0]*total_virus
DFS(0, [])

n = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            BFS(i, j, n)
            n += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            void_dict[(i, j)] = [0] * 10

results = list(void_dict.values())

for i in range(len(subset)):
    find_num(subset[i])

if answer == 9999:
    answer = -1

print(answer)