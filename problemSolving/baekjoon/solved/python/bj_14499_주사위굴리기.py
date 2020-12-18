def rolling(n):
    if n == 1:
        dice[0][0], dice[1][0], dice[1][1], dice[1][2] = dice[1][0], dice[1][1], dice[1][2], dice[0][0]
    elif n == 2:
        dice[0][0], dice[1][0], dice[1][1], dice[1][2] = dice[1][2], dice[0][0], dice[1][0], dice[1][1]
    elif n == 3:
        dice[0][0], dice[0][1], dice[1][1], dice[2][1] = dice[2][1], dice[0][0], dice[0][1], dice[1][1]
    elif n == 4:
        dice[0][0], dice[0][1], dice[1][1], dice[2][1] = dice[0][1], dice[1][1], dice[2][1], dice[0][0]


N, M, x, y, K = map(int, input().split())
board = []
dirs = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [[0]*3 for _ in range(3)]
for _ in range(N):
    board.append(list(map(int, input().split())))
move = list(map(int, input().split()))
for d in move:
    if 0 <= x + dirs[d][0] < N and 0 <= y + dirs[d][1] < M:
        x += dirs[d][0]
        y += dirs[d][1]
        if board[x][y]:
            dice[1 + dirs[d][0]][1 + dirs[d][1]] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[1 + dirs[d][0]][1 + dirs[d][1]]
        rolling(d)
        print(dice[0][0])