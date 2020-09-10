def find():
    global answer
    for cnt in range(1, 1001):
        for j in range(1, K + 1):
            if 0 > pieces[j][0] + dirs[pieces_d[j]][0] \
            or 0 > pieces[j][1] + dirs[pieces_d[j]][1] \
            or N <= pieces[j][0] + dirs[pieces_d[j]][0] \
            or N <= pieces[j][1] + dirs[pieces_d[j]][1] \
            or board[pieces[j][0] + dirs[pieces_d[j]][0]][pieces[j][1] + dirs[pieces_d[j]][1]] == 2:
                if pieces_d[j] == 1:
                    pieces_d[j] = 2
                elif pieces_d[j] == 2:
                    pieces_d[j] = 1
                elif pieces_d[j] == 3:
                    pieces_d[j] = 4
                else:
                    pieces_d[j] = 3
                if 0 > pieces[j][0] + dirs[pieces_d[j]][0] \
                or 0 > pieces[j][1] + dirs[pieces_d[j]][1] \
                or N <= pieces[j][0] + dirs[pieces_d[j]][0] \
                or N <= pieces[j][1] + dirs[pieces_d[j]][1] \
                or board[pieces[j][0] + dirs[pieces_d[j]][0]][pieces[j][1] + dirs[pieces_d[j]][1]] == 2:
                    continue
            for k in range(len(chess[(pieces[j])])):
                if j == chess[(pieces[j])][k]:
                    if not board[pieces[j][0] + dirs[pieces_d[j]][0]][pieces[j][1] + dirs[pieces_d[j]][1]]:
                        chess[(pieces[j][0] + dirs[pieces_d[j]][0], pieces[j][1] + dirs[pieces_d[j]][1])] += chess[(pieces[j])][k:]
                    else:
                        chess[(pieces[j][0] + dirs[pieces_d[j]][0], pieces[j][1] + dirs[pieces_d[j]][1])] += chess[(pieces[j])][k:][::-1]
                    if len(chess[(pieces[j][0] + dirs[pieces_d[j]][0], pieces[j][1] + dirs[pieces_d[j]][1])]) >= 4:
                        answer = cnt
                        return
                    if k > 0:
                        chess[(pieces[j])] = chess[(pieces[j])][:k]
                    else:
                        chess[(pieces[j])] = []
                    x, y = pieces[j][0] + dirs[pieces_d[j]][0], pieces[j][1] + dirs[pieces_d[j]][1]
                    for num in chess[(pieces[j][0] + dirs[pieces_d[j]][0], pieces[j][1] + dirs[pieces_d[j]][1])]:
                        pieces[num] = (x, y)
                    break



N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chess = {}
pieces = {}
pieces_d = {}
dirs = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
answer = -1
for i in range(N):
    for j in range(N):
        chess[(i, j)] = []
for i in range(1, K + 1):
    X, Y, D = map(int, input().split())
    pieces[i] = (X - 1, Y - 1)
    chess[pieces[i]] += [i]
    pieces_d[i] = D

find()
print(answer)
