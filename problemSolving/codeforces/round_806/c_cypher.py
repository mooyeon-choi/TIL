for _ in range(int(input())):
  nums = list(range(0, 10))
  num = int(input())
  state = list(map(int, input().split()))
  result = []
  for i in state:
    cnt, work = input().split()
    for w in work:
      if w == 'D':
        i += 1
      else:
        i -= 1
    result.append(str(nums[i % 10]))
  print(' '.join(result))