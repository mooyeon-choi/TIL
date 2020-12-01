T = int(input())
for _ in range(T):
  N, X = map(int, input().split())
  numList = list(map(int, input().split()))
  if min(numList) < X and numList[0] != min(numList):
    print(-1)
  else:
    newList = sorted(numList + [X])
    answer = 0
    for i in range(N - 1):
      if numList[i] != newList[i] or numList[i] != newList[i + 1]:
        if X != newList[i]:
          print(-1)
          break
        else:
          X = numList[i]
          answer += 1
    else:
      print(answer)