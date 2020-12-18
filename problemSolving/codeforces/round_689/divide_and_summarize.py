def find(num):
  if not num:
    return
  elif len(set(num)) == 1:
    result.add(sum(num))
    return
  result.add(sum(num))
  mid = (num[0] + num[-1]) / 2
  for i in range(len(num) - 1, -1, -1):
    if num[i] <= mid:
      find(num[:i+1])
      find(num[i+1:])
      return

for _ in range(int(input())):
  n, q = map(int, input().split())
  nums = sorted(list(map(int, input().split())))
  result = set()
  find(nums)
  for __ in range(q):
    print('Yes' if int(input()) in result else 'No')