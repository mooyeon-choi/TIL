def find():
    N, K = map(int, input().split())
    minX, maxX, minY, maxY = 10**5, 0, 10**5, 0
    num = []
    for __ in range(N):
      X, Y = map(int, input().split())
      num.append((X, Y))
    for i in range(N):
      for j in range(N):
        if abs(num[i][0] - num[j][0]) + abs(num[i][1] - num[j][1]) > K:
          break
      else:
        return 1
    else:
      return -1
for _ in range(int(input())):
  print(find())
  