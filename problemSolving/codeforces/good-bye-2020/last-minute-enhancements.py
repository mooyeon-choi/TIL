import sys
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  nums = list(map(int, sys.stdin.readline().split()))
  result = set()
  for i in range(len(nums)):
    if i:
      if nums[i] in result:
        result.add(nums[i] + 1)
      else:
        result.add(nums[i])
    else:
      result.add(nums[i])
  print(len(result))