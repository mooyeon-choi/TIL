n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
white = []
black = []
count = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            if count & 1:
                white.append((i, j))
            else:
                black.append((i, j))
        count += 1
