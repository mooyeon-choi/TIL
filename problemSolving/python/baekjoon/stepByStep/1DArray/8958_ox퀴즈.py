T = int(input())
for _ in range(5):
  quiz = input()
  answer, cnt = 0, 0
  for ox in quiz:
    if ox == 'O':
      cnt += 1
      answer += cnt
    else:
      cnt = 0
  print(answer)