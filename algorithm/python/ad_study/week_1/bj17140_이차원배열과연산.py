R, C, K = map(int, input().split())
board = [[0]*101 for _ in range(101)]
for i in range(3):
    board[i][0], board[i][1], board[i][2] = map(int, input().split())

width = 3
height = 3
answer = -1
for cnt in range(101):
    if board[R-1][C-1] == K:
        answer = cnt
        break
    if width <= height:
        max_width = 0
        for i in range(height):
            before = board[i][0]
            count = 1
            numlist = []
            numdict = {}
            for j in range(width):
                if board[i][j]:
                    if board[i][j] not in numdict:
                        numdict[board[i][j]] = 1
                    else:
                        numdict[board[i][j]] += 1
                    board[i][j] = 0
            for key, value in numdict.items():
                numlist.append((key, value))
            numlist.sort()
            numlist.sort(key=lambda num: num[1])
            if len(numlist) <= 50:
                for j in range(len(numlist)):
                    board[i][2*j], board[i][2*j + 1] = numlist[j][0], numlist[j][1]
                if max_width < len(numlist*2):
                    max_width = len(numlist*2)
            else:
                for j in range(50):
                    board[i][2*j], board[i][2*j + 1] = numlist[j][0], numlist[j][1]
                if max_width < 100:
                    max_width = 100
        width = max_width
    else:
        max_height = 0
        for j in range(width):
            count = 1
            numlist = []
            numdict = {}
            for i in range(height):
                if board[i][j]:
                    if board[i][j] not in numdict:
                        numdict[board[i][j]] = 1
                    else:
                        numdict[board[i][j]] += 1
                    board[i][j] = 0
            for key, value in numdict.items():
                numlist.append((key, value))
            numlist.sort()
            numlist.sort(key=lambda num: num[1])
            if len(numlist) <= 50:
                for i in range(len(numlist)):
                    board[2*i][j], board[2*i + 1][j] = numlist[i][0], numlist[i][1]
                if max_height < len(numlist*2):
                    max_height = len(numlist*2)
            else:
                for i in range(50):
                    board[2*i][j], board[2*i + 1][j] = numlist[i][0], numlist[i][1]
                if max_height < 100:
                    max_height = 100
        height = max_height


print(answer)