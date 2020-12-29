import math
for _ in range(int(input())):
  n = int(input())
  if n == 3:
    print(3, 2)
    print(3, 2)
  else:
    for i in range(n - 1, 2, -1):
      print(i, n)
    for __ in range(math.ceil(n/2)):
      print(n, 2)
