import collections as col

def BFS(i, j):
    que = col.deque()
    que.append((i, j))
    stack = []
    while que:
        u, v = que.popleft()
        visit[u][v] = 1
        stack.append((u, v))
        for k in range(4):
            if 0 <= u + dirs[k][0] < 6 and 0 <= v + dirs[k][1] < 12:
                if not visit[u + dirs[k][0]][v + dirs[k][1]] and board[i][j] == board[u + dirs[k][0]][v + dirs[k][1]]:
                    que.append((u + dirs[k][0], v + dirs[k][1]))
    if len(stack) >= 4:
        return stack
    else:
        return []

answer = -1
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
board = [['']*12 for _ in range(6)]
for i in range(11, -1, -1):
    word = input()
    for j in range(6):
        board[j][i] = word[j]
cnt = 1
while cnt:
    cnt = 0
    visit = [[0]*12 for _ in range(6)]
    remove = [[0]*12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if board[i][j] != '.' and not visit[i][j]:
                for u, v in BFS(i, j):
                    cnt += 1
                    remove[u][v] = 1
    

    answer += 1

print(answer)