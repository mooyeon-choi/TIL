import sys
sys.setrecursionlimit(100000)


def dfs(i, j, string):
    visit[i][j] = 1
    for k in range(4):
        if 0 <= i + x[k] < n and 0 <= j + y[k] < n:
            if ground[i + x[k]][j + y[k]] in string:
                if not visit[i + x[k]][j + y[k]]:
                    dfs(i + x[k], j + y[k], string)

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
n = int(input())
ground = [input() for _ in range(n)]
visit = [[0]*n for _ in range(n)]
answer = [0, 0]
for i in range(n):
    for j in range(n):
        if ground[i][j] == 'R' and not visit[i][j]:
            dfs(i, j, 'R')
            answer[0] += 1
        if ground[i][j] == 'G' and not visit[i][j]:
            dfs(i, j, 'G')
            answer[0] += 1
        if ground[i][j] == 'B' and not visit[i][j]:
            dfs(i, j, 'B')
            answer[0] += 1
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ground[i][j] != 'B' and not visit[i][j]:
            dfs(i, j, 'GR')
            answer[1] += 1
        if ground[i][j] == 'B' and not visit[i][j]:
            dfs(i, j, 'B')
            answer[1] += 1
print(*answer)
