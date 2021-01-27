def plus(num):
  for n in str(num):
    num += int(n)
  if num > 10000:
    return
  numList[num] = 0

numList = [1] * 10001
for i in range(1, 10001):
  plus(i)
for i in range(1, 10001):
  print(i) if numList[i] else None