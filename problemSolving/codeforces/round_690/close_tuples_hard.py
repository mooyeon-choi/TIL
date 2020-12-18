import sys

for _ in range(int(input())):
  n, m, k = map(int, sys.stdin.readline().split())
  nums = list(map(int, sys.stdin.readline().split()))
  nums.sort()
  answer = 0
  idx = 0
  before = 0
  if m == 1:
    print(n)
  else:
    for i in range(n - m + 1):
      if nums[i] == before:
        if idx - i >= m - 1:
          cnt = 1
          for j in range(1, m):
            cnt *= idx - i - j + 1
            cnt //= j
          answer += cnt
        continue
      else:
        before = nums[i]
        idx = i
      for j in range(i+1, n):
        if nums[j] - nums[i] > k:
          idx = j - 1
          break
      else:
        idx = j
      if idx - i >= m - 1:
        cnt = 1
        for j in range(1, m):
          cnt *= idx - i - j + 1
          cnt //= j
        answer += cnt
    print(answer)