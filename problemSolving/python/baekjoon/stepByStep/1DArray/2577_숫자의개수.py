N = 1
result = [0]*10
for _ in range(3):
  N *= int(input())
for num in str(N):
  result[int(num)] += 1
for i in range(10):
  print(result[i])