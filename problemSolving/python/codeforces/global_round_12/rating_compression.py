import sys
 
def check(N):
  if N == len(set(li)):
    M = 0
    answer = '1'
  else:
    M = N - len(set(li))
    answer = '0' * M
  n = N
  while N > 1:
    N -= 1
    used = set()
    can = True if N <= n - M else False
    for j in range(N):
      li[j] = min(li[j], li[j + 1])
      if can:
        if li[j] > N:
          can = False
        if li[j] in used:
          can = False
        else:
          used.add(li[j])
    if can:
      answer += '1'
    else:
      answer += '0'
  return answer  
 
for _ in range(int(input())):
  N = int(sys.stdin.readline())
  li = list(map(int, sys.stdin.readline().split()))
  print(check(N))