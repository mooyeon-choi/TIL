def dfs(idx, cnt, result):
  if cnt == m:
    if tuple(result) not in used:
      print(*result)
    return
  else:
    for i in range(0, n):
      if i not in idx:
        dfs(idx | {i}, cnt + 1, result + [nums[i]])

n, m = map(int, input().split())
used = set()
nums = sorted(list(map(int, input().split())))
dfs(set(), 0, [])
