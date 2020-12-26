def dfs(num, cnt):
  if cnt == m:
    return num
  else:
    return num * dfs(num - 1, cnt + 1)

n, m = map(int, input().split())
print(dfs(n, 1) // dfs(m, 1))