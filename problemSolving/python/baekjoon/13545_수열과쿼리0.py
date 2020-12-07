import sys

def find(left, right):
  l, r = left - 1, right
  maxNum = 0
  num_dict = {}
  while r > l:
    if num_list[r] in num_dict:
      if maxNum < abs(r - num_dict[num_list[r]]):
        maxNum = abs(r - num_dict[num_list[r]])
    else:
      num_dict[num_list[r]] = r
    if num_list[l] in num_dict:
      if maxNum < abs(num_dict[num_list[l]] - l):
        maxNum = abs(num_dict[num_list[l]] - l)
    else:
      num_dict[num_list[l]] = l
    r -= 1
    l += 1

  return maxNum

N = int(sys.stdin.readline())
num_list = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, len(num_list)):
  num_list[i] += num_list[i - 1]
M = int(sys.stdin.readline())
for _ in range(M):
  left, right = map(int, sys.stdin.readline().split())
  print(find(left, right))
