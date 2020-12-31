import sys
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  weight = list(map(int, sys.stdin.readline().split()))
  tree = {}
  root = set(range(1, n + 1))
  for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    if y not in tree:
      tree[y] = [x]
    else:
      tree[y].append(x)
    root.remove(x)
  
  que = []
  for num in root:
    que.append(num)

  result = []
  while que:
    nxtQue = []
    for _ in range(len(que)):
      num = que.pop()
      for i in tree[num]:
        if i in tree:
          nxtQue.append(i)
        result.append(weight[num - 1])
    que = nxtQue
  
  answer = sum(weight)
  print(answer, end=' ')
  for i in range(len(result) - 1, 0, -1):
    answer += result[i]
    print(answer, end=' ')
  print()
  
  