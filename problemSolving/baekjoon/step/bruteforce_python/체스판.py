N, M = map(int, input().split())
board = [input() for _ in range(N)]
answer = N * M
for x in range(N - 7):
  for y in range(M - 7):
    for white_start in range(2):
      cnt = 0
      for i in range(8):
        for j in range(8):
          if white_start:
            if (i + j) % 2:
              if board[x + i][y + j] != 'B':
                cnt += 1
            else:
              if board[x + i][y + j] != 'W':
                cnt += 1
          else:
            if (i + j) % 2:
              if board[x + i][y + j] != 'W':
                cnt += 1
            else:
              if board[x + i][y + j] != 'B':
                cnt += 1
      if cnt < answer:
        answer = cnt
print(answer)
