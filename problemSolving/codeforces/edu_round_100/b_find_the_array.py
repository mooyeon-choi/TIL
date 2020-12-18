import sys
import math
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  nums = list(map(int, sys.stdin.readline().split()))
  for i in range(1, n):
    if nums[i] % nums[i - 1] and nums[i - 1] % nums[i]:
      if abs(nums[i] - nums[i] // nums[i - 1] * nums[i - 1]) < abs(nums[i] - math.ceil(nums[i] / nums[i - 1]) * nums[i - 1]):
        nums[i] = nums[i] // nums[i - 1] * nums[i - 1]
      else:
        nums[i] = math.ceil(nums[i] / nums[i - 1]) * nums[i - 1]        
  print(' '.join(map(str, nums)))