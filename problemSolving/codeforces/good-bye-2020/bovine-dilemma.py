for _ in range(int(input())):
  n = int(input())
  nums = list(map(int, input().split()))
  result = set()
  for i in range(n):
    for j in range(i + 1, n):
      result.add(nums[j] - nums[i])
  print(len(result))