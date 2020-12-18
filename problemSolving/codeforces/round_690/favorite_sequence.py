for _ in range(int(input())):
  N = int(input())
  nums = input().split()
  left, right = 0, N - 1
  result = []
  if left == right:
      result.append(nums[left])
  while left < right:
    result.append(nums[left])
    result.append(nums[right])
    left += 1
    right -= 1
    if left == right:
      result.append(nums[left])
  print(' '.join(result))