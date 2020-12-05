for _ in range(int(input())):
  N = int(input())
  num = list(map(int, input().split()))
  result = 0
  maxNum = max(abs(num[-1] - num[-2]), abs(num[0] - num[1]))
  for i in range(1, N -1):
    result += abs(num[i] - num[i-1])
    if maxNum < abs(num[i] - num[i-1]) + abs(num[i+1] - num[i]) - abs(num[i+1] - num[i-1]):
        maxNum = abs(num[i] - num[i-1]) + abs(num[i+1] - num[i]) - abs(num[i+1] - num[i-1])
  result += abs(num[-1] - num[-2])
  print(result - maxNum)
