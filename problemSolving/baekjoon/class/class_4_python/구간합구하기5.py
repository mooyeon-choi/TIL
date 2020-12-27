n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
memo = [list(b) for b in board]
for i in range(n):
  for j in range(n):
    if i == 0:
      if j != 0:
        memo[i][j] += memo[i][j - 1]
    else:
      if not j:
        memo[i][j] += memo[i - 1][j]
      else:
        memo[i][j] += memo[i][j - 1] + memo[i - 1][j] - memo[i - 1][j - 1]

print(memo)
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(memo[x2 - 1][y2 - 1] - memo[x1 - 1][y1 - 1] + board[x1 - 1][y1 - 1])
