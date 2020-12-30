def dfs(idx, cnt, result):
  if cnt == m:
    if tuple(result) not in used:
      print(*result)
      used.add(tuple(result))
    return
  else:
    for i in range(idx, n):
      dfs(i, cnt + 1, result + [nums[i]])

n, m = map(int, input().split())
used = set()
nums = sorted(list(map(int, input().split())))
dfs(0, 0, [])
