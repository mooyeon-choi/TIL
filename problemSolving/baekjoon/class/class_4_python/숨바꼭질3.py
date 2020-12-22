def dfs(now, cnt):
  global answer
  if cnt >= answer or now <= 0:
    return
  if now == k:
    answer = cnt
  elif now > k:
    answer = cnt + now - k
  else:
    dfs(now * 2, cnt)
    dfs(now + 1, cnt + 1)
    dfs(now - 1, cnt + 1)

n, k = map(int, input().split())
answer = 0xffffffff
if n == k:
  print(0)
else:
  dfs(n, 0)
  print(answer)
