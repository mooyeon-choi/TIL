from pprint import pprint

for _ in range(int(input())):
  N, M = map(int, input().split())
  board = [input() for __ in range(N)]
  visit = [[0]*M for __ in range(N)]
  answer = 0
  for i in range(N - 1, -1, -1):
    for j in range(M):
      if board[i][j] == '*':
        if i == N - 1:
          visit[i][j] = 1
        else:
          if M - 1 > j and j > 0:
            visit[i][j] = 1 + min(visit[i + 1][j - 1], visit[i + 1][j], visit[i + 1][j + 1])
          else:
            visit[i][j] = 1
  pprint(sum(map(sum, visit)))
