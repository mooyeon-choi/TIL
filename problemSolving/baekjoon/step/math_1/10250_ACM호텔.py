import math
for _ in range(int(input())):
  H, W, N = map(int, input().split())
  Y = str(N % H) if N % H else str(H)
  X = str(math.ceil(N / H)) if math.ceil(N / H) > 9 else '0' + str(math.ceil(N / H))
  print(Y + X)