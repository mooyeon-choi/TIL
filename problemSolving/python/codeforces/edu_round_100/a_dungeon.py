import sys
for _ in range(int(sys.stdin.readline())):
  nums = list(map(int, sys.stdin.readline().split()))
  if not sum(nums) % 9 and min(nums) >= sum(nums) // 9:
    print('YES')
  else:
    print('NO')