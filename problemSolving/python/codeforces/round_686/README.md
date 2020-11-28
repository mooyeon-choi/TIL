# [Codeforces Round #686 (Div. 3)](https://codeforces.com/blog/entry/84957)

## 목차

* [A Special Permutation](#special-permutation)
* [B Unique Bid Auction](#unique-bid-auction)

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

* 

