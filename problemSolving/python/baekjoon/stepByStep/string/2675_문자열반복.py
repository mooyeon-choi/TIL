T = int(input())
for _ in range(T):
  N, word = map(str, input().split())
  result = ''
  for string in word:
    result += string * int(N)
  print(result)