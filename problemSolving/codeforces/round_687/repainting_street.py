T = int(input())
for _ in range(T):
  N, K = map(int, input().split())
  resultDict = {}
  cntDict = {}
  C = list(map(int, input().split()))
  for num in set(C):
    resultDict[num] = 0
    cntDict[num] = 0
  for num in C:
    for key in resultDict.keys():
      if key != num:
        cntDict[key] += 1
        if cntDict[key] >= K:
          resultDict[key] += 1
          cntDict[key] = 0
      else:
        if cntDict[key]:
          cntDict[key] += 1
          if cntDict[key] >= K:
            resultDict[key] += 1
            cntDict[key] = 0
  for key in cntDict.keys():
    if cntDict[key]:
      resultDict[key] += 1
  print(min(resultDict.values()))