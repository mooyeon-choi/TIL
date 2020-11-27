def find(left, right):
  l, r = left - 1, right - 1
  numsum = 0
  for i in range(r - l + 1):
    numsum += num_list[l+i]
  cnt = 0
  while l < r:
    l, r = left - 1, right - 1 - cnt
    nsum = numsum
    if not nsum:
      return r - l + 1
    for i in range(1, right - r):
      nsum -= num_list[l + i - 1]
      nsum += num_list[r + i]
      if not nsum:
        return r - l + 1
    else:
      cnt += 1
      numsum -= num_list[right - cnt]
  return 0

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
for _ in range(M):
  left, right = map(int, input().split())
  print(find(left, right))
