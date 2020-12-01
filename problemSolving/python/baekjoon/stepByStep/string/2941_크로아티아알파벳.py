word = input()
for repls in ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='):
  word = word.replace(repls, 'C', 100)
print(len(word))