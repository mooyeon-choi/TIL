N = int(input())
memo = [0, 0, 0]
for _ in range(N):
  colors = list(map(int, input().split()))
  memo[0], memo[1], memo[2] = colors[0] + min(memo[1], memo[2]), colors[1] + min(memo[0], memo[2]), colors[2] + min(memo[0], memo[1])
  print(memo)