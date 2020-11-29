idx, maxNum = 0, 0
for i in range(1, 10):
  num = int(input())
  if num > maxNum:
    idx, maxNum = i, num
print(f'{maxNum}\n{idx}')