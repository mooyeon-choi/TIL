def DFS(i, j):
    global answer
    if answer == 'YES':
        return
    while True:
        if (i, j, status[0], status[1]) not in visit[i][j]:
            visit[i][j].append((i, j, status[0], status[1]))
        else:
            return
        if board[i][j] in nums:
            status[0] = int(board[i][j])
            if 0 > i + dirs[status[1]][0]:
                i, j = R - 1, j
            elif R <= i + dirs[status[1]][0]:
                i, j = 0, j
            elif 0 > j + dirs[status[1]][1]:
                i, j = i, C - 1
            elif C <= j + dirs[status[1]][1]:
                i, j = i, 0
            else:
                i, j = i + dirs[status[1]][0], j + dirs[status[1]][1]
        else:
            if board[i][j] == '>':
                status[1] = 0
                if j + 1 < C:
                    i, j = i, j + 1
                else:
                    i, j = i, 0
            elif board[i][j] == '<':
                status[1] = 1
                if j - 1 >= 0:
                    i, j = i, j - 1
                else:
                    i, j = i, C - 1
            elif board[i][j] == '^':
                status[1] = 3
                if i - 1 >= 0:
                    i, j = i - 1, j
                else:
                    i, j = R - 1, j
            elif board[i][j] == 'v':
                status[1] = 2
                if i + 1 < R:
                    i, j = i + 1, j
                else:
                    i, j = 0, j
            elif board[i][j] == '_':
                if status[0]:
                    status[1] = 1
                    if j - 1 >= 0:
                        i, j = i, j - 1
                    else:
                        i, j = i, C - 1
                else:
                    status[1] = 0
                    if j + 1 < C:
                        i, j = i, j + 1
                    else:
                        i, j = i, 0
            elif board[i][j] == '|':
                if status[0]:
                    status[1] = 3
                    if i - 1 >= 0:
                        i, j = i - 1, j
                    else:
                        i, j = R - 1, j
                else:
                    status[1] = 2
                    if i + 1 < R:
                        i, j = i + 1, j
                    else:
                        i, j = 0, j
            elif board[i][j] == '.':
                if 0 > i + dirs[status[1]][0]:
                    i, j = R - 1, j
                elif R <= i + dirs[status[1]][0]:
                    i, j = 0, j
                elif 0 > j + dirs[status[1]][1]:
                    i, j = i, C - 1
                elif C <= j + dirs[status[1]][1]:
                    i, j = i, 0
                else:
                    i, j = i + dirs[status[1]][0], j + dirs[status[1]][1]
            elif board[i][j] == '@':
                answer = 'YES'
                return
            elif board[i][j] == '+':
                if status[0] == 15:
                    status[0] = 0
                else:
                    status[0] += 1
                if 0 > i + dirs[status[1]][0]:
                    i, j = R - 1, j
                elif R <= i + dirs[status[1]][0]:
                    i, j = 0, j
                elif 0 > j + dirs[status[1]][1]:
                    i, j = i, C - 1
                elif C <= j + dirs[status[1]][1]:
                    i, j = i, 0
                else:
                    i, j = i + dirs[status[1]][0], j + dirs[status[1]][1]
            elif board[i][j] == '-':
                if status[0] == 0:
                    status[0] = 15
                else:
                    status[0] -= 1
                if 0 > i + dirs[status[1]][0]:
                    i, j = R - 1, j
                elif R <= i + dirs[status[1]][0]:
                    i, j = 0, j
                elif 0 > j + dirs[status[1]][1]:
                    i, j = i, C - 1
                elif C <= j + dirs[status[1]][1]:
                    i, j = i, 0
                else:
                    i, j = i + dirs[status[1]][0], j + dirs[status[1]][1]
            elif board[i][j] == '?':
                if j + 1 < C:
                    status[1] = 0
                    DFS(i, j + 1)
                else:
                    status[1] = 0
                    DFS(i, 0)
                if j - 1 >= 0:
                    status[1] = 1
                    DFS(i, j - 1)
                else:
                    status[1] = 1
                    DFS(i, C - 1)
                if i + 1 < R:
                    status[1] = 2
                    DFS(i + 1, j)
                else:
                    status[1] = 2
                    DFS(0, j)
                if i - 1 >= 0:
                    status[1] = 3
                    DFS(i - 1, j)
                else:
                    status[1] = 3
                    DFS(R - 1, j)
                return


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for tc in range(1, int(input()) + 1):
    answer = 'NO'
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    visit = [[[] for _ in range(C)] for _ in range(R)]
    status = [0, 0]
    for i in range(R):
        for j in range(C):
            if board[i][j] == '@':
                x, y = i, j
    if x == R - 2 and y == C - 2:
        if board[x - 1][y] == '>' and board[x + 1][y] == '<' and board[x][y - 1] == '^' and board[x][y + 1] == 'v':
            print(f'#{tc} {answer}')
            continue

    if any(map(lambda x: '@' in x, board)):
        DFS(0, 0)
    print(f'#{tc} {answer}')
