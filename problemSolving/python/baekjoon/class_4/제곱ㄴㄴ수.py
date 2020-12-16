n, m = map(int, input().split())
answer = 0
result = set(range(n, m + 1))
for i in range(2, int(m**(1/2)) + 1):
  for j in range(n//i**2, m//i**2 + 1):
    if i**2 * j in result:
      result.remove(i**2 * j)
print(len(result))