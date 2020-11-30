def check(num):
  if int(num) > 99:
    between = int(num[0]) - int(num[1])
    for i in range(1, len(num) - 1):
      if between != int(num[i]) - int(num[i + 1]):
        return False
  return True

N = int(input())
answer = 0
for i in range(1, N + 1):
  answer += check(str(i))
print(answer)