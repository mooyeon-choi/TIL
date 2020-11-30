T = int(input())
for _ in range(T):
  N, P, K = map(int, input().split())
  nums = input()
  X, Y = map(int, input().split())

  numlist = {}
  for i in range(K):
    numlist[i] = Y * i
  
  for i in range(P - 1, len(nums), K):
    for j in range(K):
      if i + j >= len(nums):
        break
      if nums[i + j] == '0':
        numlist[j] += X
  
  minNum = min(numlist.values())
  print(numlist)
  for i in range(P - 1, len(nums) - K, K):
    for j in range(K):
      if i + j >= len(nums):
        break
      if nums[i + j] == '0':
        numlist[j] += -X + Y * K
      else:
        numlist[j] += Y * K
      print(numlist)
      if numlist[j] < minNum:
        minNum = numlist[j]
      
  print(minNum)
