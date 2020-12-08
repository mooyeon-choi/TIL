def find(N):
  for i in range(N):
    num = i
    for j in str(i):
      num += int(j)
    if num == N:
      return i
  return 0

print(find(int(input())))
