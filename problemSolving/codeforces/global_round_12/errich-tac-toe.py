from pprint import pprint

def findRow(i, j):
  global maxNum
  for x in range(3):
    if board[i + x][j] != 'X':
      return
  for x in range(3):
    check[i + x][j] += 1
    if check[i + x][j] > maxNum:
      maxNum = check[i + x][j]

def findCol(i, j):
  global maxNum
  for x in range(3):
    if board[i][j + x] != 'X':
      return
  for x in range(3):
    check[i][j + x] += 1
    if check[i][j + x] > maxNum:
      maxNum = check[i][j + x]

def chkBoard():
  for i in range(N):
    for j in range(N):
      if board[i][j] == 'X':
        if i < N - 2:
          findRow(i, j)
        if j < N - 2:
          findCol(i, j)

def cngBoard():
  for i in range(N):
    for j in range(N):
      if check[i][j] == maxNum:
        board[i][j] = 'O'
        return

for _ in range(int(input())):
  N = int(input())
  board = []
  for __ in range(N):
    board.append(list(input()))
  maxNum = 1
  while maxNum:
    maxNum = 0
    check = [[0]*N for ___ in range(N)]
    chkBoard()
    if maxNum: cngBoard()
  
  for i in range(N):
    print(''.join(board[i]))
