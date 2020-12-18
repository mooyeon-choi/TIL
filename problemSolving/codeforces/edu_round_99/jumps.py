def count(num, back):
  global maxCnt
  check = 0
  for i in range(1, 0xfffffff):
    if i > maxCnt:
      return
    if i <= back:
      check -= 1
    else:
      check += i
    if check >= num:
      if maxCnt > i + check - num:
        maxCnt = i + check - num
      return
  
T = int(input())
for _ in range(T):
  maxCnt = 0xfffffff
  num = int(input())
  for i in range(0xfffffff):
    if i >= maxCnt:
      break
    count(num, i)
  print(maxCnt)