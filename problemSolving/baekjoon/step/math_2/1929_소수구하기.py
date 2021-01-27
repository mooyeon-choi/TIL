M, N = map(int, input().split())
for num in range(M, N + 1):
  if num > 1:
    for i in range(2, int(num**0.5) + 1):
      if not num % i:
        break
    else:
      print(num)