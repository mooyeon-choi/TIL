for _ in range(int(input())):
  K = int(input())
  N = int(input())
  result = [i for i in range(N + 1)]
  for __ in range(K):
    for i in range(1, N + 1):
      result[i] = result[i] + result[i - 1]
  print(result[N])