N = int(input())
num = 665
cnt = 0
while True:
  num += 1
  if str(num).count('666'):
    cnt += 1
  if cnt == N:
    print(num)
    break