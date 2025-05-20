for _ in range(int(input())):
  answer = 0
  m = int(input())
  board = []
  for i in range(m):
    board.append(list(map(int, list(input()))))
 
  check = set()
  for i in range(m):
    for j in range(m):
      if (i, j) not in check:
        check.add((i, j))
        check.add((j, m - i - 1))
        check.add((m - i - 1, m - j - 1))
        check.add((m - j - 1, i))
        chkSum = board[i][j] + board[j][m - i - 1] + board[m - i - 1][m - j - 1] + board[m - j - 1][i]
        answer += chkSum if chkSum <= 2 else 4 - chkSum
      
  print(answer)