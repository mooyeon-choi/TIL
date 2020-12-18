# [Codeforces Round #686 (Div. 3)](https://codeforces.com/blog/entry/84957)

## 목차

* [A. Special Permutation](#special-permutation)
* [B. Unique Bid Auction](#unique-bid-auction)
* [C. Sequence Transformation](#sequence-transformation)

## Special Permutation

* [문제 링크](https://codeforces.com/contest/1454/problem/A)

* List의 길이가 주어지면 1 ~ List length의 숫자들이 인덱스 number와 겹치지 않게 list에 채워넣는 문제였다.

* 숫자를 순서대로 넣어주고 짝수일 경우 reverse, 홀수일 경우에는 1번 index와 가운데 숫자를 바꿔준 후 reverse를 해줘서 해결하였다.

* 풀이

  ```python
  n = int(input())
  for _ in range(n):
      num = int(input())
      nums = list(range(1, num + 1))
      if len(nums) % 2:
          nums[0], nums[len(nums) // 2] = nums[len(nums) // 2], nums[0]
          nums.reverse()
      else:
          nums.reverse()
  
      print(' '.join(map(str, nums)))
  ```

## Unique Bid Auction

* [문제 링크](https://codeforces.com/contest/1454/problem/B)

* List 에서 Unique한 가장 작은 숫자의 index 위치(index number는 1부터 시작한다)를 찾는 문제였다.

  없을 경우 -1을 출력한다.

* Set의 차집합을 활용해서 Unique한 가장 작은 숫자를 찾아주고 반복문을 통해 index를 찾아주었다.

* 풀이

  ```python
  n = int(input())
  for _ in range(n):
      c = int(input())
      nums = list(map(int, input().split()))
      numSet = set()
      removeSet = set()
      for num in nums:
          if num not in numSet:
              if num not in removeSet:
                  numSet.add(num)
          else:
              numSet.remove(num)
              removeSet.add(num)
      if numSet:
          minNum = min(numSet)
          for i in range(len(nums)):
              if nums[i] == minNum:
                  print(i + 1)
                  break
      else:
          print(-1)
  ```


## Sequence Transformation

* [문제 링크](https://codeforces.com/contest/1454/problem/C)

* 각 숫자로 리스트를 나눠주었을때 몇개로 나눠지는지 구하는 문제였다.

* Python Dictionary를 사용하여 직전 index의 숫자를 저장하고 이전의 숫자와 현재 숫자가 다를 경우 `result[현재숫자]`의 값을 증가시켜주는 방식으로 풀었다.

* 마지막 인덱스에서는 마지막 인덱스에 있는 숫자를 제외한 나머지 숫자들의 count를 모두 증가 시켜주었다.

* 풀이

  ```python
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
  ```

  

