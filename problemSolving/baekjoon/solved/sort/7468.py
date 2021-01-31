n, m = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(m):
  start, end, k = map(int, input().split())
  print(sorted(nums[start - 1:end])[k - 1])
