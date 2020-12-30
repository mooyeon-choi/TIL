def dfs(idx, cnt, result):
  if cnt == m:
    print(' '.join(result))
    return
  else:
    for i in range(idx, n):
      dfs(i, cnt + 1, result + [str(nums[i])])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
dfs(0, 0, [])
