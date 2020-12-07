M = int(input())
N = int(input())
numSet = set()
for num in range(M, N + 1):
  if num > 1:
    for i in range(2, int(num**0.5) + 1):
      if not num % i:
        break
    else:
      numSet.add(num)
if numSet:
  print(sum(numSet))
  print(min(numSet))
else:
  print(-1)