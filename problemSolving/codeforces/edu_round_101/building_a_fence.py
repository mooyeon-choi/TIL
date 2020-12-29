import sys

for _ in range(int(input())):
  n, k = map(int, sys.stdin.readline().split())
  heights = list(map(int, sys.stdin.readline().split()))
  memo = [[0, 0] for __ in range(n)]
  for i in range(n):
    if not i:
      memo[0][0] = heights[i] + 1
      memo[0][1] = heights[i] + k - 1
    elif i <= n - 2:
      if memo[i-1][1] >= heights[i] >= memo[i-1][0] - 2 * k + 1:
        memo[i][1] = min(memo[i-1][1] + k - 1, heights[i] + 2*k - 2)
        memo[i][0] = max(0, memo[i-1][0] - k + 1, heights[i] + 1)
      else:
        print('NO')
        break
    else:
      if memo[i-1][1] >= heights[i] >= memo[i-1][0] - k:
        print('YES')
      else:
        print('NO')
        break
    print(memo)