def find(num):
  cnt = 0
  for i in range(1, num + 1):
    for j in range(2):
      cnt += 1
      num -= i
      if num <= 0:
        return cnt


for _ in range(int(input())):
  X, Y = map(int, input().split())
  print(find(Y - X))