t = int(input())
for _ in range(t):
  n = int(input())
  numList = list(map(int, input().split()))
  resultDict = {numList[0]: 0}
  before = numList[0]
  for i in range(1, len(numList)):
    if i == len(numList) - 1:
      for key in resultDict.keys():
        if key != numList[i]:
          resultDict[key] += 1
    if numList[i] not in resultDict:
      resultDict[numList[i]] = 1
    else:
      if before != numList[i]:
        resultDict[numList[i]] += 1
    before = numList[i]
  print(min(resultDict.values()))