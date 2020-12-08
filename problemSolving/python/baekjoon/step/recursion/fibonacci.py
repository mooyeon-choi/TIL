# def fibo(n):
#   if n < 1: return 0
#   elif n == 1: return n
#   return fibo(n - 1) + fibo(n - 2)

# print(fibo(int(input())))

N = int(input())
result = []
for i in range(N + 1):
  if len(result) < 2:
    result.append(i)
  else:
    fibo1 = result.pop()
    fibo2 = result.pop()
    if i != N:
      result.append(fibo1)
    result.append(fibo1 + fibo2)
else:
  print(result[-1])