import sys
import operator
from functools import reduce

def nCr(n, r):
  return reduce(operator.mul, range(n, n-r, -1), 1) // reduce(op.mul, range(1, r + 1), 1)

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
          answer += nCr(idx - i, m - 1)
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
        answer += nCr(idx - i, m - 1)
    print(answer % (10**9 + 7))