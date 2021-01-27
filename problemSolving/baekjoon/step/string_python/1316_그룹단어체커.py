answer = 0
for _ in range(int(input())):
  word = input()
  before, used = '', set()
  for string in word:
    if not before:
      before = string
      continue
    if before != string:
      used.add(before)
      before = string
      if string in used:
        break
  else:
    answer += 1
print(answer)