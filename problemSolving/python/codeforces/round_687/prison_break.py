T = int(input())
for _ in range(T):
  N, M, R, C = map(int, input().split())
  w = max(N - R, R - 1)
  h = max(M - C, C - 1)
  print(w + h)