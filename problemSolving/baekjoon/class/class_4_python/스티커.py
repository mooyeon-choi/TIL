for _ in range(int(input())):
  n = int(input())
  board = [list(map(int, input().split())) for __ in range(2)]
  for i in range(1, n):
    if i == 1:
      board[0][i] += board[1][i - 1]
      board[1][i] += board[0][i - 1]
    else:
      board[0][i] += max(board[1][i - 1], board[1][i - 2])
      board[1][i] += max(board[0][i - 1], board[0][i - 2])
  print(max(board[0][-1], board[1][-1]))