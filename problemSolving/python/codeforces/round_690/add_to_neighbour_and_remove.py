for _ in range(int(input())):
  n = int(input())
  nums = list(map(int, input().split()))
  idx = 1
  check = False
  while not check:
    if idx == n:
      cnt = idx - 1
      check = True
    num = sum(nums[:idx])
    numsum = 0
    cnt = idx - 1
    for i in range(idx, n):
      numsum += nums[i]
      if numsum == num:
        numsum = 0
      elif numsum > num:
        break
      else:
        cnt += 1
    else:
      if not numsum:
        check = True
    idx += 1
  print(cnt)
