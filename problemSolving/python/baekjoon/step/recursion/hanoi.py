def hanoi(n, start, between, end):
  if n == 1:
    print(start, end)
    return
  hanoi(n - 1, start, end, between)
  print(start, end)
  hanoi(n - 1, between, start, end)

N = int(input())
print(2**N - 1)
hanoi(N, 1, 2, 3)