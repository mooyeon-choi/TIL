from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def BFS():
    que = deque([(0, 0)])
    while que:
        i, j = que.popleft()
        for d in range(4):
            if 0 <= i + dirs[d][0] < N and 0 <= j + dirs[d][1] < M:
                if not change[i + dirs[d][0]][j + dirs[d][1]]:
                    if board[i + dirs[d][0]][j + dirs[d][1]]:
                        change[i + dirs[d][0]][j + dirs[d][1]] = 1
                    else:
                        change[i + dirs[d][0]][j + dirs[d][1]] = 1
                        que.append((i + dirs[d][0], j + dirs[d][1]))

def cng():
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] and change[i][j]:
                board[i][j] = 0
                count += 1
    return count

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while sum(map(lambda b: sum(b), board)):
    change = [[0] * M for _ in range(N)]
    BFS()
    nums = cng()
    answer += 1

print(answer)
print(nums)