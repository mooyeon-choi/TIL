A = int(input())
B = input()
results = [A * int(B[i]) for i in range(len(B) - 1, -1, -1)] + [A * int(B)]
for result in results:
  print(result)