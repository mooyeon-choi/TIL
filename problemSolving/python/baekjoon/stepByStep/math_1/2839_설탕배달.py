N = int(input())
for i in range(N//5, -1, -1):
  if not (N - 5 * i) % 3:
    print(i + (N - 5 * i) // 3)
    break
else:
  print(-1)
