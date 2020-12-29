for _ in range(int(input())):
  n = int(input())
  nnums = list(map(int, input().split()))
  m = int(input())
  mnums = list(map(int, input().split()))
  nmax = 0
  mmax = 0
  cnt = 0
  for num in nnums:
    cnt += num
    if cnt > nmax:
      nmax = cnt
  cnt = 0
  for num in mnums:
    cnt += num
    if cnt > mmax:
      mmax = cnt
  print(nmax + mmax)