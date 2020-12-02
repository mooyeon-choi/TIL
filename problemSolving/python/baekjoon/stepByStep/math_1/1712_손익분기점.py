import math

A, B, C = map(int, input().split())
if B >= C:
  print(-1)
else:
  print(math.trunc(A/(C - B)) + 1)