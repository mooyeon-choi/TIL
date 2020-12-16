import sys

for _ in range(int(input())):
  n = int(sys.stdin.readline())
  nums = list(map(int, sys.stdin.readline().split()))
  nums.sort()
  answer = 0
  idx = 0
  before = 0
  for i in range(n - 2):
    if nums[i] == before:
      if idx - i >= 2:
        answer += (idx - i) * (idx - i - 1) // 2
      continue
    else:
      before = nums[i]
      idx = i
    for j in range(i+1, n):
      if nums[j] - nums[i] > 2:
        idx = j - 1
        break
    else:
      idx = j
    if idx - i >= 2:
      answer += (idx - i) * (idx - i - 1) // 2
  print(answer)