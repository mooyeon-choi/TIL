for _ in range(int(input())):
  n = int(input())
  word = input()
  cnt = 0
  for i in range(len(word) - 1, -1, -1):
    if word[i] != ')':
      break
    else:
      cnt += 1
  if not cnt or n / cnt >=2:
    print('NO')
  else:
    print('YES')
  