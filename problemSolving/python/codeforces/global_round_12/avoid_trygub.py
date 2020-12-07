for _ in range(int(input())):
  N = int(input())
  word = input()
  for i in range(len(word)):
    if word[i] == 'b':
      word = 'b' + word[:i] + word[i+1:]
  print(word)