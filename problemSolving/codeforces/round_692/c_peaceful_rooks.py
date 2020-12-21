import sys
for _ in range(int(sys.stdin.readline())):
  n, m = map(int, sys.stdin.readline().split())
  rooks = []
  cnt = {}
  used = set()
  for __ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == j:
      used.add(i)
      m -= 1
      continue
    rooks.append((i, j))
    if i not in cnt:
      cnt[i] = 1
    else:
      cnt[i] += 1
    if j not in cnt:
      cnt[j] = 1
    else:
      cnt[j] += 1
  for u in used:
    cnt[u] = 9
  if m - list(cnt.values()).count(1) <= 0:
    print(m)
  else:
    print(m + 1)