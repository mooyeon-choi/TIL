nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def find(num, idx):
  if sum(num) == n:
    result.append(''.join(map(str,num)))
  elif sum(num) > n or idx > 9:
    return
  for i in range(idx, 10):
    find(num + [nums[i]], i + 1)

for _ in range(int(input())):
  n = int(input())
  result = []
  find([], 0)
  print(min(map(int, result)) if result else -1)
  