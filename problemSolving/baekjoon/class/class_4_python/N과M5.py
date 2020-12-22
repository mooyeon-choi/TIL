def dfs(numlist, cnt):
  if cnt == m:
    print(' '.join(map(str, numlist)))
    return
  for i in range(0, len(nums)):
    if nums[i] not in numlist:
      dfs(numlist + [nums[i]], cnt + 1)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
dfs([], 0)