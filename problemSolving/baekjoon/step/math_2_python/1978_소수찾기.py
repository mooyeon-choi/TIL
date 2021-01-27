N = int(input())
answer = 0
for num in map(int, input().split()):
  if num > 1:
    for i in range(2, int(num**0.5) + 1):
      if not num % i:
        break
    else:
      answer += 1
print(answer)