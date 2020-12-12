string = ['a', 'b', 'c']
for _ in range(int(input())):
  N, K = map(int, input().split())
  word = ''
  idx = 0
  while len(word) < N:
    if len(word) + K < N:
      word = word + string[idx % 3]*K
    else:
      word = word + string[idx % 3] * (N - len(word))
    idx += 1
  print(word)