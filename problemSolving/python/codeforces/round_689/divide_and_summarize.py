import sys
sys.setrecursionlimit(100000)

def find(left, right):
  if left >= right:
    return
  elif len(set(nums[left:right])) == 1:
    result.add(sum(nums[left:right]))
    return
  result.add(sum(nums[left:right]))
  mid = (nums[left] + nums[right - 1]) / 2
  for i in range(left, right):
    if nums[i] > mid:
      find(left, i)
      find(i, right)
      return

for _ in range(int(input())):
  n, q = map(int, input().split())
  nums = sorted(list(map(int, input().split())))
  result = set()
  find(0, n)
  for __ in range(q):
    print('Yes' if int(input()) in result else 'No')