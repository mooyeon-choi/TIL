result = ['-1'] * 26
word = input()
for i in range(len(word)):
  if result[ord(word[i]) - 97] == '-1':
    result[ord(word[i]) - 97] = str(i)
print(' '.join(result))