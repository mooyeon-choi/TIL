import sys
sys.setrecursionlimit(1000000)


def find():
    for key, value in shark.items():
        board[value[0]][value[1]] = key


def move():
    for key, value in shark.items():
        dist = shark_info[key][0]
        x, y = tuple(shark[key])
        if shark_info[key][1] < 3:
            while 0 > x + dirs[shark_info[key][1]][0] * dist or x + dirs[shark_info[key][1]][0] * dist >= R:
                if 0 > x + dirs[shark_info[key][1]][0] * dist:
                    dist, x, shark_info[key][1] = dist - x, 0, 2
                elif x + dirs[shark_info[key][1]][0] * dist >= R:
                    dist, x, shark_info[key][1] = dist - R + x + 1, R - 1, 1
            if shark_info[key][1] == 1:
                x = x - dist
                compare(x, y, key)
            else:
                x = x + dist
                compare(x, y ,key)
        else:
            while 0 > y + dirs[shark_info[key][1]][1] * dist or y + dirs[shark_info[key][1]][1] * dist >= C:
                if 0 > y + dirs[shark_info[key][1]][1] * dist:
                    dist, y, shark_info[key][1] = dist - y, 0, 3
                elif y + dirs[shark_info[key][1]][1] * dist >= C:
                    dist, y, shark_info[key][1] = dist - C + y + 1, C - 1, 4
            if shark_info[key][1] == 3:
                y = y + dist
                compare(x, y, key)
            else:
                y = y - dist
                compare(x, y, key)


def compare(x, y, key):
    if board[x][y]:
        if board[x][y] < key:
            if board[x][y] not in remove:
                remove.append(board[x][y])
            board[x][y] = key
            shark[key] = [x, y]
        else:
            if board[x][y] not in remove:
                remove.append(key)
    else:
        board[x][y] = key
        shark[key] = [x, y]


dirs = [0, (-1, 0 ), (1, 0), (0, 1), (0, -1)]
R, C, M = map(int, input().split())
shark = {}
shark_info = {}
answer = 0
board = [[0] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[z] = [r-1, c-1]
    shark_info[z] = [s, d]

find()
for cnt in range(C):
    remove = []
    for i in range(R):
        if board[i][cnt]:
            answer += board[i][cnt]
            shark.pop(board[i][cnt])
            break
    board = [[0] * C for _ in range(R)]
    move()
    for num in remove:
        shark.pop(num)

print(answer)