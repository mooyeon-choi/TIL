import sys
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  while True:
    for num in set(str(n)):
      if num != '0' and n % int(num):
        break
    else:
      print(n)
      break
    n -= 1