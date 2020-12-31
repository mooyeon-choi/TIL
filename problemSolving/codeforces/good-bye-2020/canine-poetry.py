import sys
for _ in range(int(sys.stdin.readline())):
  words = list(sys.stdin.readline())
  answer = 0
  for i in range(1, len(words) - 1):
    if i == 1:
      if words[i] == words[i - 1]:
        words[i] = ' '
        answer += 1
    else:
      if words[i] == words[i - 1] or words[i] == words[i - 2]:
        words[i] = ' '
        answer += 1
  print(words)
  print(answer)