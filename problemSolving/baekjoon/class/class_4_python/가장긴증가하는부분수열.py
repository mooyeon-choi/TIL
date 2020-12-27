def dfs(idx, cnt):
  global answer
  if idx == -1:
    num = 0
  else:
    num = nums[idx]
  for i in range(idx + 1, n):
    if nums[i] > num:
      dfs(i, cnt + 1)
  if cnt > answer:
    answer = cnt

answer = 0
n = int(input())
nums = list(map(int, input().split()))
dfs(-1, 0)
print(answer)