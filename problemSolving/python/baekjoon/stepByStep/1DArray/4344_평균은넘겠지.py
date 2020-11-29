T = int(input())
for _ in range(T):
  N, *scores = map(int, input().split())
  average = sum(scores) / N
  result = 0
  for score in scores:
    if score > average:
      result += 1
  result = str(round(result / N * 100, 3)).split('.')
  result[1] += '0' * (3 - len(result[1]))
  print('.'.join(result) + '%')