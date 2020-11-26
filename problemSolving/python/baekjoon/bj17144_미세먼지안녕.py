def findCleaner():
    for i in range(R):
        if board[i][0] == -1:
            air_cleaner.append((i, 0))
            air_cleaner.append((i + 1, 0))
            return



def spray():
    for i in range(R):
        for j in range(C):
            if board[i][j] > 4:
                use = board[i][j] // 5
                for k in range(4):
                    if 0 <= i + dirs[k][0] < R and 0 <= j + dirs[k][1] < C and board[i + dirs[k][0]][j + dirs[k][1]] != -1:
                        dust[i + dirs[k][0]][j + dirs[k][1]] += use
                        board[i][j] -= use

def spread():
    for i in range(R):
        for j in range(C):
            board[i][j] += dust[i][j]
            dust[i][j] = 0


def move():
    top_before = 0
    bot_before = 0
    for i in range(1, C):
        top_before, board[air_cleaner[0][0]][i] = board[air_cleaner[0][0]][i], top_before
        bot_before, board[air_cleaner[1][0]][i] = board[air_cleaner[1][0]][i], bot_before
    i = 1
    while air_cleaner[0][0] - i >= 0:
        top_before, board[air_cleaner[0][0] - i][C-1] = board[air_cleaner[0][0] - i][C-1], top_before
        i += 1
    i = 1
    while air_cleaner[1][0] + i < R:
        bot_before, board[air_cleaner[1][0] + i][C - 1] = board[air_cleaner[1][0] + i][C - 1], bot_before
        i += 1
    for i in range(1, C):
        top_before, board[0][C - i - 1] = board[0][C - i - 1], top_before
        bot_before, board[R-1][C - i - 1] = board[R-1][C - i - 1], bot_before
    i = 1
    while board[i][0] != -1:
        top_before, board[i][0] = board[i][0], top_before
        i += 1
    i = 2
    while board[R-i][0] != -1:
        bot_before, board[R-i][0] = board[R-i][0], bot_before
        i += 1

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
dust = [[0]*C for _ in range(R)]
air_cleaner = []

findCleaner()
for _ in range(T):
    spray()
    spread()
    move()

print(sum(map(lambda x: sum(x), board), 2))