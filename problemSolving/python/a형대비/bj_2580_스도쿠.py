board = [list(map(int, input().split())) for _ in range(9)]

count = 1
numset = set([1,2,3,4,5,6,7,8,9])
while count:
    count = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                count += 1
                nset = set([])
                for x in range(3):
                    for y in range(3):
                        nset.add(board[i][x*3+y])
                        nset.add(board[x*3+y][j])
                        nset.add(board[i//3*3+x][j//3*3+y])
                canset = numset - nset
                if len(canset) == 1:
                    board[i][j] = sum(canset)
for i in range(9):
    print(*board[i]

