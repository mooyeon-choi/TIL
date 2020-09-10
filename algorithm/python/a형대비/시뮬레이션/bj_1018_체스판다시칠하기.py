line = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

def checkLine(X, Y):
    W_first = 0
    B_first = 0
    for i in range(8):
        for j in range(8):
            if board[X + i][Y + j] != line[i % 2][j]:
                W_first += 1
            if board[X + i][Y + j] != line[(i + 1) % 2][j]:
                B_first += 1
    return min(W_first, B_first)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
answer = 64

for i in range(N - 7):
    for j in range(M - 7):
        num = checkLine(i, j)
        if answer > num:
            answer = num

print(answer)