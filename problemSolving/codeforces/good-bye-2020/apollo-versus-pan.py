import sys
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  nums = list(map(int, sys.stdin.readline().split()))
  answer = 0
  modulo = 1000000007
  for i in range(n):
    for j in range(n):
      for k in range(n):
        answer += (nums[i] & nums[j]) * (nums[j] | nums[k])
        if answer > modulo:
          answer %= modulo
  print(answer)