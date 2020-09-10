def DFS(x, y, vertex):
    if len(vertex) == 1:
        for u in range(1, N - y):
            DFS(x+u, y+u, vertex + [(x+u, y+u)])
    if len(vertex) == 2:
        for u in range(1, N - x):
            DFS(x+u, y-u, vertex + [(x+u, y-u)])
    if len(vertex) == 3:
        for u in range(1, x + 1):
            if x + y - 2 * u < i + j or y - u < 0:
                return
            elif x + y - 2 * u == i + j:
                subset.append(vertex + [(x-u, y-u)])
        return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0xffffff
region = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
subset = []
population = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
numsum = 0
answer = 0xffffff

for i in range(N - 2):
    for j in range(1, N):
        DFS(i, j, [(i, j)])

for sub in subset:
    population[1], population[2], population[3], population[4], population[5] = 0, 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if i + j < sub[0][0] + sub[0][1] and j <= sub[0][1] and i < sub[3][0]:
                population[1] += board[i][j]
            elif i + j > sub[1][0] + sub[1][1] and j >= sub[2][1] and i > sub[1][0]:
                population[4] += board[i][j]
            elif i - j > sub[3][0] - sub[3][1] and j < sub[2][1] and i >= sub[3][0]:
                population[3] += board[i][j]
            elif i - j < sub[0][0] - sub[0][1] and j > sub[0][1] and i <= sub[1][0]:
                population[2] += board[i][j]
            else:
                population[5] += board[i][j]
    numsum = max(population.values()) - min(population.values())
    if numsum < answer:
        answer = numsum

print(answer)

